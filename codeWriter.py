class CodeWriter:
    def __init__(self,outName:str):
        # Opens the output file
        self._outBaseName=outName.split("/")[-1]
        self._arithmeticCount=1
        self._returnIndex=0
        self._outFile=open(outName,"a")
        self._segmentPointers=["LCL","ARG","THIS","THAT"]
        self._segmentMap={
            "local":self._segmentPointers[0],
            "argument":self._segmentPointers[1],
            "this":self._segmentPointers[2],
            "that":self._segmentPointers[3]
        }


    # Writes assembly bootstrap code
    def writeBootstrap(self):
        # SP = 256
        self._outFile.write(self._writeLines([
            "// SP = 256",
            "@256",
            "D=A",
            "@SP",
            "M=D"
        ]))

        # Call sys init
        self.writeCall("Sys.init",0)

    # Writes to the output file the assembly code, that implements the given arithmetic command
    def writeArithmetic(self,command):
        code = self._writeLines([" ".join(["//",command])])
        match command:
            case "add" | "sub":
               code+=self._writeLines(
                    [
                        "@SP",
                        "AM=M-1", 
                        "D=M", 
                        "@SP", 
                        "AM=M-1",
                        "M=M"+("+D" if command=="add" else "-D"),     
                    ]
                )
            case "neg" | "not":
                code+=self._writeLines(
                    [
                        "@SP",
                        "AM=M-1",
                        "M="+ ("-M" if command == "neg" else "!M") ,
                    ]
                )
            case "and" | "or":
                code+=self._writeLines(
                    [
                        "@SP",
                        "AM=M-1",
                        "D=M",
                        "@SP",
                        "AM=M-1",
                        "M=M"+("&" if command == "and" else "|")+"D", 
                    ]
                )
            case "eq" | "gt" | "lt":
                jump = "JEQ"
                if command == "gt":
                    jump = "JGT"
                elif command == "lt":
                    jump = "JLT"
                upperCommand=command.upper()
                code+=self._writeLines(
                    [
                        "@SP",
                        "AM=M-1", 
                        "D=M", 
                        "@SP",
                        "AM=M-1",
                        "D=M-D",
                        "@" + upperCommand + "_TRUE_"+str(self._arithmeticCount),
                        "D;" + jump,
                        "@SP",
                        "A=M",
                        "M=0",
                        "@" + upperCommand + "_END_"+str(self._arithmeticCount),
                        "0;JMP",
                    ])+self._writeLines(
                    [
                        "(" + upperCommand + "_TRUE_"+str(self._arithmeticCount)+")"
                    ]
                        ,0)+self._writeLines([
                        "@SP",
                        "A=M",
                        "M=-1"
                    ])+self._writeLines([
                        "(" + upperCommand + "_END_"+str(self._arithmeticCount)+")"
                    ],0)
                self._arithmeticCount+=1
                
        code+=self._writeLines(
            [
                "@SP", 
                "M=M+1"
            ]
        )
        self._outFile.write(code)

    # Writes to the output file the assembly code, that implements the given push or pop command
    # command -> C_PUSH or C_POP
    # segment -> constant, local etc.
    # index
    def writePushPop(self,command,segment,index):
        code=""
        
        match command:
            case "C_PUSH":
                
                # push implementation
                code+=self._writeLines([" ".join(["//","push",segment,str(index)])])

                # if segment == "local" | "argument" | "this" | "that"
                if  segment in ["local","this","argument","that"]:
                    code+=self._pushLatt(segment,index)

                # if segment == "constant"
                elif segment=="constant":
                    code+=self._pushConstant(index)

                # if segment == "temp"
                elif segment == "temp":
                    code+=self._pushTemp(index)

                # if segment == "static"
                elif segment == "static":
                    code+=self._pushStatic(index)

                # if segment == "pointer"
                else:
                    code+=self._pushPointer(index)
            case "C_POP":
                
                # pop implementation
                code+=self._writeLines([" ".join(["//","pop",segment,str(index)])])

                # if segment == "local" | "argument" | "this" | "that"
                if  segment in ["local","this","argument","that"]:
                    code+=self._popLatt(segment,index)

                # if segment == "static"
                elif segment == "static":
                    code+=self._popStatic(index)

                # if segment == "temp"
                elif segment == "temp":
                    code+=self._popTemp(index)
                # if segment == "pointer"
                else:
                    code+=self._popPointer(index)
        self._outFile.write(code)
    
    # Writes assembly code that effects the label command
    def writeLabel(self,label:str):
        self._outFile.write(self._writeLines([
            "("+label+")"
        ],0))
    
    # Writes assembly code that effects the goto command
    def writeGoto(self,label:str):
        self._outFile.write(self._writeLines([
            "// goto "+label,
            "@"+label,
            "0;JMP"
        ]))

    # Writes assembly code that effects the if-goto command
    def writeIf(self,label:str):
        self._outFile.write(self._writeLines([
            "// if-goto "+label,
            "@SP",
            "AM=M-1",
            "D=M",
            "@"+label,
            "D;JNE"
        ]))


    # Writes assembly code that effects the function command
    def writeFunction(self,functionName:str,nVars:int):
        self._outFile.write(self._writeLines([
            "("+functionName+")"
        ],0))
        # push constant 0 n times
        for i in range(nVars):
            self.writePushPop("C_PUSH","constant",0)
        
    
    # Writes assembly code that effects the call command
    def writeCall(self,functionName:str,nVars:int):
        
        # generate return address label
        returnLabel = functionName+"$ret."+str(self._returnIndex)
        self._returnIndex+=1
        
        # push returnAddress
        code=self._writeLines([
            "// call "+functionName+" "+str(nVars),
            "@"+returnLabel,
            "D=A",
            "@SP",
            "A=M",
            "M=D",
            "@SP",
            "M=M+1"
        ])


        # Save the caller states in the stack
        # push LCL, ARG, THIS, THAT
        for segmentPointer in self._segmentPointers:
            code+=self._writeLines([
                "@"+segmentPointer,
                "D=M",
                "@SP",
                "A=M",
                "M=D",
                "@SP",
                "M=M+1"
            ])

        # Reposition ARG
        # ARG = SP-5-nArgs
        code+=self._writeLines([
            "@SP",
            "D=M",
            "@5",
            "D=D-A",
            "@"+str(nVars),
            "D=D-A",
            "@ARG",
            "M=D"
        ])

        # LCL = SP
        code+=self._writeLines([
            "@SP",
            "D=M",
            "@LCL",
            "M=D"
        ])
        self._outFile.write(code)

        # goto fnName
        self.writeGoto(functionName)

        # write return address label
        self._outFile.write(self._writeLines([
            "("+returnLabel+")"
        ],0))
    
    # Writes assembly code that effects the return command
    def writeReturn(self):

        # Save return address
        code=self._writeLines([
            "// return",
            "@LCL",
            "D=M",
            "@5",
            "D=D-A",
            "A=D",
            "D=M",
            "@retAddr",
            "M=D"
        ])   

        # Sets the return value and resets the stack pointer
        # *ARG=*(SP-1), SP=ARG+1
        code+=self._writeLines([
            "@SP",
            "AM=M-1",
            "D=M",
            "@ARG",
            "A=M",
            "M=D",
            "@ARG",
            "D=M+1",
            "@SP",
            "M=D"
        ])

        # Reset segment pointers
        segmentPointersRev = self._segmentPointers[::-1]
        for i in range(4):
            segmentPointer=segmentPointersRev[i]
            code+=self._writeLines([
                "// Set "+segmentPointer,
                "@"+str(i+1),
                "D=A",
                "@LCL",
                "A=M-D",
                "D=M",
                "@"+segmentPointer,
                "M=D"
            ])

        code+=self._writeLines([
            "@retAddr",
            "A=M",
            "0;JMP"
        ])
        self._outFile.write(code)
    
    def setFileName(self,filename:str):
        # self._returnIndex=0
        pass

    # Push local | argument | this | that i
    # addr = segmentPointer+index, *SP=*addr, SP++
    def _pushLatt(self,segment,index):
        return self._writeLines(
                    [
                       "@"+str(index),
                       "D=A",
                       "@"+self._segmentMap[segment],
                       "A=M+D",
                       "D=M",
                       "@SP",
                       "A=M",
                       "M=D",
                       "@SP",
                       "M=M+1"
                    ]
                )
    
    # Pop local | argument | this | that i
    # addr = segmentPointer+index,  SP--, *addr=*SP
    def _popLatt(self,segment,index):
        return self._writeLines(
                    [
                        "@"+str(index),
                        "D=A",
                        "@"+self._segmentMap[segment],
                        "D=M+D",
                        "@addr",
                        "M=D",
                        "@SP",
                        "AM=M-1",
                        "D=M",
                        "@addr",
                        "A=M",
                        "M=D"
                    ]
                )

    # push constant i
    # *SP=i, SP++
    def _pushConstant(self,index):
        return self._writeLines(
            [
                "@"+str(index),
                "D=A",
                "@SP",
                "A=M",
                "M=D",
                "@SP",
                "M=M+1"
            ]
        )
    
    # pop static i
    # SP--, xxx.i = *SP

    def _popStatic(self,index):
        return self._writeLines(
            [
                "@SP",
                "AM=M-1",
                "D=M",
                "@"+self._outBaseName.replace(".asm","."+str(index)),
                "M=D"
            ]
        )
    
    # push static i
    # SP*=xxx.i, SP++

    def _pushStatic(self,index):
        return self._writeLines(
            [
                "@"+self._outBaseName.replace(".asm","."+str(index)),
                "D=M",
                "@SP",
                "A=M",
                "M=D",
                "@SP",
                "M=M+1"
            ]
        )
    
    # addr = 5+index, *SP=addr, SP++
    def _pushTemp(self,index):
        return self._writeLines(
            [
                "@"+str(index+5),
                "D=M",
                "@SP",
                "A=M",
                "M=D",
                "@SP",
                "M=M+1"
            ]
        )
    
    # addr = 5+index,  SP--, addr=*SP
    def _popTemp(self,index):
        return self._writeLines(
            [
                "@SP",
                "AM=M-1",
                "D=M",
                "@"+str(index+5),
                "M=D"
            ]
        )
    
    # push pointer 0/1
    # *SP = THIS/THAT, SP++
    def _pushPointer(self,index):
        segment="THIS" if index == 0 else "THAT"
        return self._writeLines(
            [
                "@"+segment,
                "D=M",
                "@SP",
                "A=M",
                "M=D",
                "@SP",
                "M=M+1"
            ]
        )

    # pop pointer 0/1
    # SP--, THIS/THAT = *SP
    def _popPointer(self,index):
        segment="THIS" if index == 0 else "THAT"
        return self._writeLines(
            [
                "@SP",
                "AM=M-1",
                "D=M",
                "@"+segment,
                "M=D"
            ]
        )
    
    def _writeLines(self,lines:list,indent=4):
        indentation=" "*indent
        return "\n".join(map(lambda line:indentation+line,lines))+"\n"
    
    def end(self):
        # self._outFile.write(self._writeLines(["(END)"],0)+self._writeLines(["@END","0;JMP"]))
        self.close()

    # Closes the output file
    def close(self):
        self._outFile.close()
        
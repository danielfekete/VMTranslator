class CodeWriter:
    def __init__(self,outName:str):
        # Opens the output file
        self._outName=outName
        self._outFile=open(outName,"a")
        self._segmentMap={
            "local":"LCL",
            "argument":"ARG",
            "this":"THIS",
            "that":"THAT"
        }

    # Writes to the output file the assembly code, that implements the given arithmetic command
    def writeArithmetic(self,command):
        match command:
            case "add":
                return "A+D"
        
    # Writes to the output file the assembly code, that implements the given push or pop command
    # command -> C_PUSH or C_POP
    # segment -> constant, local etc.
    # index
    def writePushPop(self,command,segment,index):
        code=""
        match command:
            case "C_PUSH":
                # push implementation

                # if segment == "local" | "argument" | "this" | "that"
                if ["local","this","argument","that"] in segment:
                    code+=self._pushLatt(segment,index)

                # if segment == "constant"
                elif segment=="constant":
                    code+=self._pushConstant(index)

                # if segment == "temp"
                elif segment == "temp":
                    code+=self._pushTemp(index)

                # if segment == "pointer"
                else:
                    code+=self._pushPointer(index)
                return
            case "C_POP":
                # pop implementation

                # if segment == "local" | "argument" | "this" | "that"
                if ["local","this","argument","that"] in segment:
                    code+=self._popLatt(segment,index)

                # if segment == "static"
                elif segment == "static":
                    code+=self._popStatic(index)

                # if segment == "temp"
                if segment == "temp":
                    code+=self._popTemp(index)
                # if segment == "pointer"
                else:
                    code+=self._popPointer(index)
                return
    
    # Push local | argument | this | that i
    # addr = segmentPointer+index, *SP=*addr, SP++
    def _pushLatt(self,segment,index):
        return "\n".join(
                    [
                        " ".join(["//","push",segment,index]),
                       "@"+index,
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
        return "\n".join(
                    [
                        " ".join(["//","pop",segment,index]),
                        "@"+index,
                        "D=A",
                        "@"+self._segmentMap[segment],
                        "M=M+D",
                        "@SP",
                        "AM=M-1",
                        "D=M",
                        "@"+self._segmentMap[segment],
                        "A=M",
                        "M=D"
                    ]
                )

    # push constant i
    # *SP=i, SP++
    def _pushConstant(self,index):
        return "\n".join(
            [
                " ".join("//","push","constant",index),
                "@"+index,
                "D=A",
                "@SP",
                "A=M",
                "M=D",
                "@SP",
                "M=M+1"
            ]
        )
    
    # pop static i
    # xxx.i = *SP

    def _popStatic(self,index):
        return "\n".join(
            [
                " ".join("//","pop","static",index),
                "@SP",
                "A=M",
                "D=M",
                "@"+self._outName.replace(".asm","."+index),
                "M=D"
            ]
        )
    
    # addr = 5+index, *SP=*addr, SP++
    def _pushTemp(self,index):
        return self._pushLatt("temp",index+5)
    
    # addr = 5+index,  SP--, *addr=*SP
    def _popTemp(self,index):
        return self._popLatt("temp",index+5)
    
    # push pointer 0/1
    # *SP = THIS/THAT, SP++
    def _pushPointer(self,index):
        segment="THIS" if index == 0 else "THAT"
        return "\n".join(
            [
                " ".join("//","push","pointer",index),
                "@"+segment,
                "D=A",
                "@SP",
                "A=M",
                "M=D",
                "@SP"
                "M=M+1"
            ]
        )

    # pop pointer 0/1
    # SP--, THIS/THAT = *SP
    def _popPointer(self,index):
        segment="THIS" if index == 0 else "THAT"
        return "\n".join(
            [
                " ".join("//","pop","pointer",index),
                "@SP",
                "AM=M-1",
                "D=M",
                "@"+segment,
                "M=D"
            ]
        )

    # Closes the output file
    def close(self):
        self._outFile.close()
        
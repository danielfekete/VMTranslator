class CodeWriter:
    def __init__(self,outName:str):
        # Opens the output file
        self._outFile=open(outName,"a")

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
        segmentMap={
            "local":"LCL",
            "argument":"ARG",
            "this":"THIS",
            "that":"THAT"
        }
        match command:
            case "C_PUSH":
                # push implementation

                # if segment = "local" | "argument" | "this" | "that"
                # addr = SP+index, *SP=*addr, SP++
                code+="\n".join(
                    [
                        " ".join(["//","push",segment,index]),
                       "@"+index,
                       "D=A",
                       "@"+segmentMap[segment],
                       "A=M+D",
                       "D=M",
                       "@SP",
                       "A=M",
                       "M=D",
                       "@SP",
                       "M=M+1"
                    ]
                )
                return
            case "C_POP":
                # pop implementation

                # if segment = "local" | "argument" | "this" | "that"
                # addr = SP+index,  SP--, *addr=*SP
                code+="\n".join(
                    [
                        " ".join(["//","pop",segment,index]),
                        "@"+index,
                        "D=A",
                        "@"+segmentMap[segment],
                        "M=M+D",
                        "@SP",
                        "AM=M-1",
                        "D=M",
                        "@"+segmentMap[segment],
                        "A=M",
                        "M=D"
                    ]
                )
                return
    # Closes the output file
    def close(self):
        self._outFile.close()
        
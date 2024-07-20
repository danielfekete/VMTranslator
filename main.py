import sys
import os
import instructionParser
import codeWriter

def main():
    # opens the input file
    src = sys.argv[1]
    # create the output file
    outName = src.replace(".vm",".asm")
    if os.path.exists(outName):
        os.remove(outName)
    # Construct parser and writer classes
    parser=instructionParser.InstructionParser(src)
    writer=codeWriter.CodeWriter(outName)

    while parser.hasMoreLines():
        parser.advance()
        commandType = parser.commandType()
        arg1=parser.arg1()
        
        if  commandType in ["C_PUSH","C_POP"]:
            # Write push or pop operations
            arg2=parser.arg2()
            writer.writePushPop(commandType,arg1,arg2)
        else:
            # Write arithmetic operations   
            writer.writeArithmetic(arg1)
    writer.close()

if __name__ == "__main__":
    main()
                

import sys
import os
import instructionParser
import codeWriter



class Main:
    def main():
        src = sys.argv[1]
    
        # Check if the source path exists
        if not os.path.exists:
            print("Invalid folder/file path")
            return
        
        # Check if the source path is a directory
        isDir = os.path.isdir(src)

        # Create the otuput vm file name
        outName = src.replace(".vm",".asm") if not isDir else os.path.join(src,src.split('/')[-1]+".asm")

        

        # Check if the output file is already exists
        if os.path.exists(outName):
            # Remove the output file
            os.remove(outName)

        # Construct parser
        writer=codeWriter.CodeWriter(outName)

        # Parse the source file(s) and write the .asm commands
        if not isDir:
            parseAndWriteCommands(writer,src)
        else:
            # Bootstrap the os
            writer.writeBootstrap()
            # Loop through the .vm files
            directory = os.fsencode(src)
            for file in os.listdir(directory):
                filename = os.fsdecode(file)
                if filename.endswith(".vm"):
                    writer.setFileName(filename)
                    parseAndWriteCommands(writer,os.path.join(src,filename))
        writer.end()


def parseAndWriteCommands(writer:codeWriter.CodeWriter,src:str):
        parser=instructionParser.InstructionParser(src)
        while parser.hasMoreLines():
            parser.advance()
            commandType = parser.commandType()
            arg1=parser.arg1()

            # Handle command types
            match commandType:
                case "C_PUSH" | "C_POP":
                    arg2=parser.arg2()
                    writer.writePushPop(commandType,arg1,arg2)
                case "C_LABEL":
                    writer.writeLabel(arg1)
                case "C_GOTO":
                    writer.writeGoto(arg1)
                case "C_IF":
                    writer.writeIf(arg1)
                case "C_FUNCTION":
                    arg2=parser.arg2()
                    writer.writeFunction(arg1,arg2)
                case "C_CALL":
                    arg2=parser.arg2()
                    writer.writeCall(arg1,arg2)
                case "C_RETURN":
                    writer.writeReturn()
                case _:
                    # Write arithmetic operations   
                    writer.writeArithmetic(arg1)

if __name__ == "__main__":
    Main.main()
                

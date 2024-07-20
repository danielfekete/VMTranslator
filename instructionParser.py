import re

class InstructionParser:
    def __init__(self,src:str):
        # opens the input file
        self._inputFile = open (src,'r')
        self._currentInstruction = ""

    # read next line
    # this method should be called only if hasMoreLines() is true
    def advance(self):
        while True:
            line=self._inputFile.readline()
            # When instruction is valid (not empty line or a comment) set the current instruction and return
            if re.match(r"^[\s]*$|^[\s]*\/\/.*$",line) == None:
                # Set the new instruction
                self._currentInstruction=line.strip()
                return
            # return if the src file doesn't have more lines 
            elif self.hasMoreLines() == False:
                return
    
    # checks if the file has more lines
    def hasMoreLines(self)->bool:
        # Get the current position
        currentPosition = self._inputFile.tell()
        hasMoreLines = False
        if self._inputFile.readline() != "":
            hasMoreLines = True
        # Reset the current position
        self._inputFile.seek(currentPosition)
        return hasMoreLines
    
    # Returns the type of the current command
    def commandType(self)->str:
        match = re.match(r"(push|pop|label|goto|if-goto|function|return|call)",self._currentInstruction) 
        if match:
            if match[1] == "if-goto":
                return "C_IF"
            return "C_" + match[1].upper()
        return "C_ARITHMETIC"

    # Returns the first argument of the current command        
    def arg1(self)->str:
        return self._currentInstruction if self.commandType() == "C_ARITHMETIC" else self._currentInstruction.split()[1]
    
    # Returns the second argument of the current command        
    def arg2(self)->int:
        return int(self._currentInstruction.split()[2])


    
    
    
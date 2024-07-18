import sys
import os
import re

def main():
    # opens the input file
    src = sys.argv[1]
    # create the output file
    outName = src.replace(".vm",".asm")
    if os.path.exists(outName):
        os.remove(outName)
    out = open(outName,"a")
(SimpleFunction.test)
    // push constant 0
    @0
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    // push constant 0
    @0
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    // push local 0
    @0
    D=A
    @LCL
    A=M+D
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    // push local 1
    @1
    D=A
    @LCL
    A=M+D
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    // add
    @SP
    AM=M-1
    D=M
    @SP
    AM=M-1
    M=M+D
    @SP
    M=M+1
    // not
    @SP
    AM=M-1
    M=!M
    @SP
    M=M+1
    // push argument 0
    @0
    D=A
    @ARG
    A=M+D
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    // add
    @SP
    AM=M-1
    D=M
    @SP
    AM=M-1
    M=M+D
    @SP
    M=M+1
    // push argument 1
    @1
    D=A
    @ARG
    A=M+D
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    // sub
    @SP
    AM=M-1
    D=M
    @SP
    AM=M-1
    M=M-D
    @SP
    M=M+1
    // return
    @LCL
    D=M
    @5
    D=D-A
    A=D
    D=M
    @retAddr
    M=D
    @SP
    AM=M-1
    D=M
    @ARG
    A=M
    M=D
    @ARG
    D=M+1
    @SP
    M=D
    // Set THAT
    @1
    D=A
    @LCL
    A=M-D
    D=M
    @THAT
    M=D
    // Set THIS
    @2
    D=A
    @LCL
    A=M-D
    D=M
    @THIS
    M=D
    // Set ARG
    @3
    D=A
    @LCL
    A=M-D
    D=M
    @ARG
    M=D
    // Set LCL
    @4
    D=A
    @LCL
    A=M-D
    D=M
    @LCL
    M=D
    @retAddr
    A=M
    0;JMP

    // push constant 0
    @0
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    // pop local 0
    @0
    D=A
    @LCL
    D=M+D
    @addr
    M=D
    @SP
    AM=M-1
    D=M
    @addr
    A=M
    M=D
(LOOP)
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
    // add
    @SP
    AM=M-1
    D=M
    @SP
    AM=M-1
    M=M+D
    @SP
    M=M+1
    // pop local 0
    @0
    D=A
    @LCL
    D=M+D
    @addr
    M=D
    @SP
    AM=M-1
    D=M
    @addr
    A=M
    M=D
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
    // push constant 1
    @1
    D=A
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
    // pop argument 0
    @0
    D=A
    @ARG
    D=M+D
    @addr
    M=D
    @SP
    AM=M-1
    D=M
    @addr
    A=M
    M=D
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
    // if-goto LOOP
    @SP
    AM=M-1
    D=M
    @LOOP
    D;JNE
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
(END)
    @END
    0;JMP

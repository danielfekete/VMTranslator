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
    // pop pointer 1
    @SP
    AM=M-1
    D=M
    @THAT
    M=D
    // push constant 0
    @0
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    // pop that 0
    @0
    D=A
    @THAT
    D=M+D
    @addr
    M=D
    @SP
    AM=M-1
    D=M
    @addr
    A=M
    M=D
    // push constant 1
    @1
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    // pop that 1
    @1
    D=A
    @THAT
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
    // push constant 2
    @2
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
    // if-goto COMPUTE_ELEMENT
    @SP
    AM=M-1
    D=M
    @COMPUTE_ELEMENT
    D;JNE
    // goto END
    @END
    0;JMP
(COMPUTE_ELEMENT)
    // push that 0
    @0
    D=A
    @THAT
    A=M+D
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    // push that 1
    @1
    D=A
    @THAT
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
    // pop that 2
    @2
    D=A
    @THAT
    D=M+D
    @addr
    M=D
    @SP
    AM=M-1
    D=M
    @addr
    A=M
    M=D
    // push pointer 1
    @THAT
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
    // add
    @SP
    AM=M-1
    D=M
    @SP
    AM=M-1
    M=M+D
    @SP
    M=M+1
    // pop pointer 1
    @SP
    AM=M-1
    D=M
    @THAT
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
    // goto LOOP
    @LOOP
    0;JMP
(END)

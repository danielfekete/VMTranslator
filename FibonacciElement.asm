    // SP = 256
    @256
    D=A
    @SP
    M=D
    @Sys.init$ret.0
    A=D
    @SP
    A=M
    M=D@SP
    M=M+1
    @LCL
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @ARG
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THIS
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THAT
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @5
    D=A
    @SP
    D=A-D
    @0
    D=D-A
    @ARG
    M=D
    @SP
    D=M
    @LCL
    M=D
    // goto Sys.init
    @Sys.init
    0;JMP
(@Sys.init$ret.0)
(Main.fibonacci)
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
    // lt
    @SP
    AM=M-1
    D=M
    @SP
    AM=M-1
    D=M-D
    @LT_TRUE_1
    D;JLT
    @SP
    A=M
    M=0
    @LT_END_1
    0;JMP
(LT_TRUE_1)
    @SP
    A=M
    M=-1
(LT_END_1)
    @SP
    M=M+1
    // if-goto N_LT_2
    @SP
    AM=M-1
    D=M
    @N_LT_2
    D;JNE
    // goto N_GE_2
    @N_GE_2
    0;JMP
(N_LT_2)
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
(N_GE_2)
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
    @Main.fibonacci$ret.0
    A=D
    @SP
    A=M
    M=D@SP
    M=M+1
    @LCL
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @ARG
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THIS
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THAT
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @5
    D=A
    @SP
    D=A-D
    @1
    D=D-A
    @ARG
    M=D
    @SP
    D=M
    @LCL
    M=D
    // goto Main.fibonacci
    @Main.fibonacci
    0;JMP
(@Main.fibonacci$ret.0)
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
    @Main.fibonacci$ret.0
    A=D
    @SP
    A=M
    M=D@SP
    M=M+1
    @LCL
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @ARG
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THIS
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THAT
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @5
    D=A
    @SP
    D=A-D
    @1
    D=D-A
    @ARG
    M=D
    @SP
    D=M
    @LCL
    M=D
    // goto Main.fibonacci
    @Main.fibonacci
    0;JMP
(@Main.fibonacci$ret.0)
    // add
    @SP
    AM=M-1
    D=M
    @SP
    AM=M-1
    M=M+D
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
(Sys.init)
    // push constant 4
    @4
    D=A
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @Main.fibonacci$ret.0
    A=D
    @SP
    A=M
    M=D@SP
    M=M+1
    @LCL
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @ARG
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THIS
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @THAT
    D=M
    @SP
    A=M
    M=D
    @SP
    M=M+1
    @5
    D=A
    @SP
    D=A-D
    @1
    D=D-A
    @ARG
    M=D
    @SP
    D=M
    @LCL
    M=D
    // goto Main.fibonacci
    @Main.fibonacci
    0;JMP
(@Main.fibonacci$ret.0)
(END)
    // goto END
    @END
    0;JMP

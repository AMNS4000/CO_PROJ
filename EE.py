#----READING THE FILE----
import sys
# l1=sys.stdin.read().splitlines()
# f1=open("Output.txt","w")
# f1.close()
MEMLIST=["0000000000000000"]*256
print(MEMLIST,sep="\n")
PC_NO="00000000"
halted=False

def btod(str):
    a=str
    num=0
    p=0
    for i in a:
        num+=int(i)*2**p
        p+=1
    return num

def btod(str):
    a=int(str)
    num=0
    p=0
    for i in a:
        num+=i*p
        p+=1
    return num


def MEM():
    return
def EE():
    instruction=MEM[int(PC_NO)]
    code=instruction[5]
    if (code=="10000"):
        R1="R"+str(btod(instruction[7:10]))
        R2="R"+str(btod(instruction[10:13]))
        R3="R"+str(btod(instruction[13:16]))
        addition(R1,R2,R3)
    elif(code=="10001"):
        R1="R"+str(btod(instruction[7:10]))
        R2="R"+str(btod(instruction[10:13]))
        R3="R"+str(btod(instruction[13:16]))
        subtraction(R1,R2,R3)
    elif(code=="10010"):
        R1="R"+str(btod(instruction[5:8]))
        imm=instruction[8:16]
        move_imm(R1,imm)
    elif(code=="10011"):
        R1="R"+str(btod(instruction[10:13]))
        R2="R"+str(btod(instruction[13:16]))
        move_reg(R1,R2)
    elif(code=="10100"):
        R1="R"+str(btod(instruction[5:8]))
        memadress=instruction[8:16]
        Load(R1,memadress)
    elif(code=="10101"):
        R1="R"+str(btod(instruction[5:8]))
        memadress=instruction[8:16]
        Store(R1,memadress)
    elif(code=="10110"):
        R1="R"+str(btod(instruction[7:10]))
        R2="R"+str(btod(instruction[10:13]))
        R3="R"+str(btod(instruction[13:16]))
        multiply(R1,R2,R3)
    elif(code=="10111"):
        R1="R"+str(btod(instruction[10:13]))
        R2="R"+str(btod(instruction[13:16]))
        divide(R1,R2)
    elif(code=="11000"):
        R1="R"+str(btod(instruction[5:8]))
        imm=instruction[8:16]
        right_shift(R3,imm)
    elif(code=="11001"):
        R1="R"+str(btod(instruction[5:8]))
        imm=instruction[8:16]
        left_shift(R3,imm)
    elif(code=="11010"):
        R1="R"+str(btod(instruction[7:10]))
        R2="R"+str(btod(instruction[10:13]))
        R3="R"+str(btod(instruction[13:16]))
        XOR(R1,R2,R3)
    elif(code=="11011"):
        R1="R"+str(btod(instruction[7:10]))
        R2="R"+str(btod(instruction[10:13]))
        R3="R"+str(btod(instruction[13:16]))
        OR(R1,R2,R3)
    elif(code=="11100"):
        R1="R"+str(btod(instruction[7:10]))
        R2="R"+str(btod(instruction[10:13]))
        R3="R"+str(btod(instruction[13:16]))
        AND(R1,R2,R3)
    elif(code=="11101"):
        R1="R"+str(btod(instruction[10:13]))
        R2="R"+str(btod(instruction[13:16]))
        INV(R1,R2)
    elif(code=="11110"):
        R1="R"+str(btod(instruction[10:13]))
        R2="R"+str(btod(instruction[13:16]))
        compare(R1,R2)
    elif(code=="11111"):
        memadress=instruction[8:16]
        uncoditional_jump(memadress)
    elif(code=="01100"):
        memadress=instruction[8:16]
        jumpless(memadress)
    elif(code=="01101"):
        memadress=instruction[8:16]
        jumpgreat(memadress)
    elif(code=="01111"):
        memadress=instruction[8:16]
        jumpequal(memadress)
    elif(code=="01010"):
        halted=True
    # PC_NO=str(int(PC_NO)+1)
    return 

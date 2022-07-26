#----READING THE FILE----
import sys
'''import sys
f1=sys.stdin.read().splitlines()''' 

list1=[]
f1=open("Output.txt","r")
code=f1.read().splitlines()
for i in code:
    #print(i)
    list1.append(i)
f1.close()

def MEM(PC):
    return(list1[PC])
MEMLIST=["0000000000000000"]*256
print(MEMLIST,sep="\n")
PC_NO=0
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

for i in MEMLIST:
    if i[5]=="01010":
        haltline=MEMLIST.index(i)

RF={"R1":"0"*16,"R2":"0"*16,"R3":"0"*16,"R4":"0"*16,"R5":"0"*16,"R6":"0"*16,"FLAGS":"0"*16}
FLAGS=["0"]*16

def dtob(n):
    x=""
    while int(n)!=0:
        x+=str(int(n)%2)
        n=str(int(n)//2)
    return x[::-1]

def btod(n):
    x=n[::-1]
    s=0
    for i in range(len(n)):
        s+=(2**(i))*(int(x[i]))
    return s

def addition(reg1, reg2, reg3):
    val1=btod(RF[str(reg1)])
    val2=btod(RF[str(reg2)])
    if (val1+val2>2**16-1):
        FLAGS[12]="1"
    else:
        str3=dtob(val1+val2)
        if (len(str3)==16):
            RF[str(reg3)]=str3
        elif (len(str3)!=16):
            RF[str(reg3)]="0"*(16-len(str3))+str3
    PC_NO+=1        
    
def subtraction(reg1, reg2, reg3):
    val1=btod(RF[str(reg1)])
    val2=btod(RF[str(reg2)])
    if (val1<val2):
        FLAGS[13]=1
        reg3="0"*16
    else:
        str3=dtob(val1-val2)
        if (len(str3)==16):
            RF[str(reg3)]=str3
        elif (len(str3)!=16):
            RF[str(reg3)]="0"*(16-len(str3))+str3
    PC_NO+=1

def multiplication(reg1, reg2, reg3):
    val1=btod(RF[str(reg1)])
    val2=btod(RF[str(reg2)])
    if (val1*val2>2**16-1):
        FLAGS[14]="1"
    else:
        str3=dtob(val1*val2)
        if (len(str3)==16):
            RF[str(reg3)]=str3
        elif (len(str3)!=16):
            RF[str(reg3)]="0"*(16-len(str3))+str3
    PC_NO+=1

def jumpless(mem):
    if (FLAGS[-3]=="1"):
        if (mem>=haltline):
            print("halt passed")
            return 0
        else:   
            PC_NO=mem
    else:
        PC_NO+=1

def jumpequal(mem):
    if (FLAGS[-3]=="1"):
        if (mem>=haltline):
            print("halt passed")
            return 0
        else:   
            PC_NO=mem
    else:
        PC_NO+=1

def jumpgreat(mem):
    if (FLAGS[-3]=="1"):
        if (mem>=haltline):
            print("halt passed")
            return 0
        else:   
            PC_NO=mem
    else:
        PC_NO+=1

def unconditional_jump(mem):
    if (mem>=haltline):
        print("halt passed")
        return 0
    else:   
        PC_NO=mem

def INV(R1,R2):
    Rx=btod(RF[str(R1)])
    RF[str(R2)]=~bin(Rx)
    PC_NO+=1

def AND(R1,R2,R3):
    RF[str(R3)] = RF[str(R2)] & RF [str(R1)]
    PC_NO+=1


def OR(R1,R2,R3):
    RF[str(R3)] = RF[str(R2)] | RF [str(R1)]
    PC_NO+=1
    

def XOR(R1,R2,R3):
    RF[str(R3)] = RF[str(R2)] ^ RF [str(R1)]
    PC_NO+=1

def left_shift(R1,imm):
    temp=RF[str(R1)]
    temp[:8]=temp[8:]
    temp[8:]=imm
    PC_NO+=1


def right_shift(R1,imm):
    temp=RF[str(R1)]
    temp[8:]=temp[:8]
    temp[:8]=imm
    PC_NO+=1

def divide(R3,R4):
    x=btod(RF[str[R3]])
    y=btod(RF[str[R4]])
    RF["R0"]=dtob(x//y)
    RF["R1"]=dtob(x%y)
    PC_NO+=1


def EE(instruction):
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
        unconditional_jump(memadress)
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

while (not halted):
    instruction=MEM(PC_NO)
    EE(instruction)
    

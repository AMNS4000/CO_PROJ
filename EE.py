#----READING THE FILE----
import sys
'''import sys
f1=sys.stdin.read().splitlines()''' 
list1=[]
f1=open("output.txt","r")
code=f1.read().splitlines()
for i in code:
    #print(i)
    list1.append(i)
f1.close()

print(list1)
PC_NO=0
def MEM(PC):
    return(list1[PC_NO])

# MEML=["0000000000000000"]*256
# print(MEMLIST,sep="\n")
haltline=0
for i in list1:
    if i[:5]=="01010":
        haltline=list1.index(i)

RF={"R0":"0"*16,"R1":"0"*16,"R2":"0"*16,"R3":"0"*16,"R4":"0"*16,"R5":"0"*16,"R6":"0"*16,"R7":"0"*16}
FLAGS=["0"]*16
RF["R0"]="0000000000000001"
RF["R1"]="0000000000000001"
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
    
    global PC_NO
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
    global PC_NO
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
    global PC_NO
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
def moveimmediate(reg1,val):
    global PC_NO
    RF[str(reg1)]="0"*8+val
    PC_NO+=1
def moveregister(reg1,reg2):
    global PC_NO
    if (str(reg1)=="R7" or str(reg2)=="R7"):
        RF[str(reg2)]="".join(FLAGS)
    else:
        RF[str(reg2)]=RF[str(reg1)]
    PC_NO+=1
def Load(reg1,mem_addr):
    global PC_NO
    RF[str(reg1)]=list1[btod(mem_addr)]
    PC_NO+=1
def Store(reg1,mem_addr):
    global PC_NO
    list1[btod(mem_addr)]=RF[str(reg1)]
    PC_NO+=1
def jumpless(mem):
    global PC_NO
    if (FLAGS[-3]=="1"):
        if (mem>=haltline):
            print("halt passed")
            return 0
        else:   
            PC_NO=mem
    else:
        PC_NO+=1

def jumpequal(mem):
    global PC_NO
    if (FLAGS[-2]=="1"):
        if (mem>=haltline):
            print("halt passed")
            return 0
        else:   
            PC_NO=mem
    else:
        PC_NO+=1

def jumpgreat(mem):
    global PC_NO
    if (FLAGS[-1]=="1"):
        if (btod(mem)>=haltline):
            print("halt passed")
            return 0
        else:   
            PC_NO=mem
    else:
        PC_NO+=1

def unconditional_jump(mem):
    global PC_NO
    if (mem>=haltline):
        print("halt passed")
        return 0
    else:   
        PC_NO=mem

def INV(R1,R2):
    global PC_NO
    Rx=btod(RF[str(R1)])
    RF[str(R2)]=~bin(Rx)
    PC_NO+=1

def AND(R1,R2,R3):
    global PC_NO
    RF[str(R3)] = RF[str(R2)] & RF [str(R1)]
    PC_NO+=1

def OR(R1,R2,R3):
    global PC_NO
    RF[str(R3)] = RF[str(R2)] | RF [str(R1)]
    PC_NO+=1
    

def XOR(R1,R2,R3):
    global PC_NO
    RF[str(R3)] = RF[str(R2)] ^ RF [str(R1)]
    PC_NO+=1

def left_shift(R1,imm):
    global PC_NO
    temp=RF[str(R1)]
    temp[:8]=temp[8:]
    temp[8:]=imm
    PC_NO+=1


def right_shift(R1,imm):
    global PC_NO
    temp=RF[str(R1)]
    temp[8:]=temp[:8]
    temp[:8]=imm
    PC_NO+=1

def divide(R3,R4):
    global PC_NO
    x=btod(RF[str[R3]])
    y=btod(RF[str[R4]])
    RF["R0"]=dtob(x//y)
    RF["R1"]=dtob(x%y)
    PC_NO+=1
def compare(reg1,reg2):
    global PC_NO
    if (RF[str(reg1)]>RF[str(reg2)]):
        FLAGS[-2]="1"
    elif (RF[str(reg1)]<RF[str(reg2)]):
        FLAGS[-3]="1"
    elif (RF[str(reg1)]==RF[str(reg2)]):
        FLAGS[-1]="1"
    PC_NO+=1

halted=False

def EE(instruction):
    global halted
    code=instruction[:5]
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
        moveimmediate(R1,imm)
    elif(code=="10011"):
        R1="R"+str(btod(instruction[10:13]))
        R2="R"+str(btod(instruction[13:16]))
        moveregister(R1,R2)
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
        multiplication(R1,R2,R3)
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
        if (not unconditional_jump(memadress)):
            halted=True
    elif(code=="01100"):
        memadress=instruction[8:16]
        if (not jumpless(memadress)):
            halted=True
    elif(code=="01101"):
        memadress=instruction[8:16]
        if (not jumpgreat(memadress)):
            halted=True
    elif(code=="01111"):
        memadress=instruction[8:16]
        if (not jumpequal(memadress)):
            halted=True
    elif(code=="01010"):
        halted=True
    # PC_NO=str(int(PC_NO)+1)
    return 

while (not halted):
    instruction=MEM(PC_NO)
    EE(instruction)
    print(PC_NO,end=" ")    
    for i in RF.values():
        print(i,end=" ")
    print("\n")
    
for i in list1:
    print(i,end="\n")
    

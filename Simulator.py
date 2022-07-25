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
    return True
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
    return True
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
    return True








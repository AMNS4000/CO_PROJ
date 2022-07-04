#---FUNCTION FOR CONVERTING DECIMAL TO BINARY----   
# def getb(n,size):
#     ns=""
#     print(n,size)
#     while int(n)!=1:
#         ns+=str(n%2)
#         n=n//2
#     ns+=str(n)
#     if (len(ns)<size):
#         return ((size-len(ns))*"0"+ns[::-1])
#     return ns[::-1]

#---DEFINING DIFFERENT SYMBOLS LIST
regd=[ "R0", "R1" , "R2" , "R3" , "R4" , "R5" , "R6"]
labeld=["hlt"]
var={}
errordict={1:"Wrong immediate value has to be an integer and in the range [0,255]",
           2:"Labels cannot be used in place of variables",
           3:"Invalid register used",
           4:"hlt statement not present",
           5:"Incorrect way to write the instruction syntax error",
           6:"undefined variable",
           7:"invalid use of Flags register",
           8:"$ sign absent when writing immediate values",
           9:"undefined label",
           10:"wrong syntax for hlt instruction"}

#---DIFFERENT FUNCTIONS FOR HANDLING ALL SORTS OF ERRORS---
def checkimmediatevalue(n):
    if (isinstance(n,int)==False):
        return False
    elif (n<0 or n>255):
        return False
    else:
        return True
def checklengthofInstuct(l1,str1):
    if (str1=="TypeA"):
        if (len(l1)!=4):
            return False
    elif (str1=="TypeB" or str1=="TypeC" or str1=="TypeD"):
        if (len(l1)!=3):
            return False
    elif (str1=="TypeE"):
        if (len(l1)!=2):
            return False
    elif (str1=="TypeF"):
        if (len(l1)!=1):
            return False
    else:
        return True
def checkdollar(str2):
    if (str2=="$"):
        return True
    else:
        return False
def checkoverflow(b1,b2):
    if (b1+b2<255):
        return True
    else:
        return False
def useofFLAGS(l1):
    if (l1[1]=="FLAGS"):
        return False
    else:
        return True
def checkcorrectregister(l1,str3):
    if (str3=="TypeA"):
        for i in range(1,len(l1)):
            if (l1[i] not in regd):
                return False
    elif (str3=="TypeB" or str3=="TypeC"):
        if (l1[1] not in regd):
            return False
    else:
        return True
def heckuseoflabels(l1):
    if (l1[2] in labeld):
        return False
    else:
        return True
def checkuseofvariable(l1):
    if (l1[2] not in var.keys()):
        return False
    else:
        return True

getb= lambda x, n: format(x, 'b').zfill(n)
def TypeA(str): 
    TypeA={"add":"10000","sub":"10001","mul":"10110","xor":"11010","or":"11011","and":"11100"}
    un="00"
    ns=TypeA[str[0]]+un+getb(int(str[1][1]),3)+getb(int(str[2][1]),3)+getb(int(str[3][1]),3)
    return ns+"\n"

def TypeB(str): 
    TypeB={"mov":"10010","rs":"11000","ls":"11001"}
    reg1s=getb(int(s[1][1]),3)
    ns=TypeB[str[0]]+reg1s+getb(int(str[2][1:]),8)
    return ns+"\n"

def TypeC(str): 
    TypeC={"div":"10111","mov":"10100","not":"11101","cmp":"11110"}
    reg1s=getb(int(s[1][1]),3)
    reg2s=getb(int(s[2][1]),3)
    ns=TypeC[str[0]]+"00000"+reg1s+reg2s
    return ns+"\n"

def TypeD(str): 
    TypeD={"ld":"10100","st":"10101"}
    reg1s=getb(int(s[1][1]),3)
    print(str[2])
    ns=TypeD[str[0]]+reg1s+var[str[2]]
    return ns+"\n"

def TypeE(str): 
    TypeE={"jmp":"11111","jlt":"01100","jgt":"01101","je":"01111"}
    ns=TypeE[str[0]]+"000"+str[1]
    return ns+"\n"

f=open("Desktop/New Folder/q.txt",'r')  #change file path accordingly
Lta=["add","sub","mul","xor","or","and"]
Ltb=["mov","rs","ls"]
Ltc=["div","mov","not","cmp"]
Ltd=["ld","st"]
Lte=["jmp","jlt","jgt","je"]
L=["add","sub","mul","xor","or","and","mov","rs","ls","div","mov","not","cmp","ld","st","jmp","jlt","jgt","je"]
def check(str2):
    if str2[0] in Lta:
        print(TypeA(str2))
    elif str2[0] in Ltb :
        if str2[0]!="mov":
            print(TypeB(str2))
        elif str2[0]=="mov" and str2[2][0]=="$":
            print(TypeB(str2))
    if str2[0] in Ltc:
        if str2[0]!="mov":
            print(TypeC(str2))
        elif str2[0]=="mov" and str2[2][0]=="R":
            print(TypeC(str2))
    elif str2[0] in Ltd:
        print(TypeD(str2))
    
    elif str2[0] in Lte:
        print(TypeE(str2))

line_count=1

F=f.readlines()
cnt=0
for i in F:
    while (i[0]=="var"):
        cnt+=1
n=len(F)-cnt
varchk=0
for i in F:
    s=i.split()
    print(i)
    if s[0]=="var" :
        if varchk==0:
            var[s[1]]=getb(n,8)
            n+=1
        elif varchk==1:
            print("Error")
    elif s[0] in L:
        varchk=1
        check(s)
    elif s[0][-1]==":":
        labeld.append(s.pop(0))
        check(s)
    elif s[0] =="hlt":
        print("0101000000000000")
    line_count+=1 
print(line_count)
f.close()
print(labeld)



####   DOUBTS
#Do we need to count var instructions for program counter?

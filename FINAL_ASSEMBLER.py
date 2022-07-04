#----READING THE FILE----
f1=open("q.txt","r")
l1=f1.read().splitlines()
#---FUNCTION FOR CONVERTING DECIMAL TO BINARY----   
def dtob(n,size):
    ns=""
    while int(n)!=1:
        ns+=str(n%2)
        n=n//2
    ns+=str(n)
    if (len(ns)<size):
        return ((size-len(ns))*"0"+ns[::-1])
    return ns[::-1]
#---DEFINING DIFFERENT SYMBOLS LIST
regd=[ "R0", "R1" , "R2" , "R3" , "R4" , "R5" , "R6"]
vard={}
labeld={}
errordict={1:"Wrong immediate value has to be an integer and in the range [0,255]",
           2:"Labels cannot be used in place of variables",
           3:"Invalid register used",
           4:"hlt statement not present",
           5:"Incorrect way to write the instruction syntax error",
           6:"undefined variable",
           7:"invalid use of Flags register",
           8:"$ sign absent when writing immediate values",
           9:"undefined label",
           10:"wrong syntax for hlt instruction",
           11:"Variables cannot be used in place of labels",
           12:"undefined label",
           13:"Variable definition after instruction"}
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
                return i
    elif (str3=="TypeB" or str3=="TypeC"):
        if (l1[1] not in regd):
            return False
    else:
        return True
def checkuseoflabelsinpvariables(l1):
    if (l1[1] in labeld.keys()):
        return False
    else:
        return True
def checkuseofvariable(l1):
    if (l1[2] not in vard.keys()):
        return False
    else:
        return True
def checkuseoflabels(l1):
    if (l1 not in labeld.keys()):
        return False
    else:
        return True
def checkuseofvariablesinplabels(l1):
    if (l1[1] in vard.keys()):
        return False
    else:
        return True
def typeAerr(l1):
    if (checklengthofInstuct(l1,"TypeA")==False):
        ns=errordict[5]+"for"+str(l1[0])
        return ns
    elif (useofFLAGS(l1)==False):
        return errordict[7]
    elif (checkcorrectregister(l1,"TypeA")==False):
        return "register"+str(l1[checkcorrectregister(11,"TypeA")])+"does not exist and is invalid"
    else:
        return True
def typeBerr(l1):
    if (checklengthofInstuct(l1,"TypeB")==False):
        ns=errordict[5]+"for"+str(l1[0])
        return ns
    elif (useofFLAGS(l1)==False):
        return errordict[7]
    elif (checkcorrectregister(l1,"TypeB")==False):
        return "register"+str(l1[1])+"does not exist and is invalid"
    elif (checkdollar(l1[2][0])==False):
        return errordict[8]
    elif (checkimmediatevalue(int(l1[2][1:]))==False):
        return errordict[1]
    else:
        return True
def typeCerr(l1):
    if (checklengthofInstuct(l1,"TypeC")==False):
        ns=errordict[5]+"for"+str(l1[0])
        return ns
    elif (useofFLAGS(l1)==False):
        return errordict[7]
    elif (checkcorrectregister(l1,"TypeC")==False):
        return "register"+str(l1[1])+"does not exist and is invalid"
    elif (l1[1]=="mov"):
        l2=l1[1:]
        if (checkcorrectregister(l2)==False):
            return "register"+str(l1[2])+"does not exist and is invalid"
    else:
        return True
def typeDerr(l1):
    if (checklengthofInstuct(l1,"TypeD")==False):
        ns=errordict[5]+"for"+str(l1[0])
        return ns
    elif (checkuseoflabelsinpvariables(l1)==False):
        return errordict[2]
    elif (checkuseofvariable(l1)==False):
        return errordict[6]
    else:
        return True
def typeEerr(l1):
    if (checklengthofInstuct(l1,"TypeE")==False):
        ns=errordict[5]+"for"+str(l1[0])
        return ns
    elif (checkuseofvariablesinplabels(l1)==False):
        return errordict[11]
    elif (checkuseoflabels(ln)==False):
        return errordict[12]
    else:
        return True
def typeFerr(l1,ln):
    if (checklengthofInstuct(l1,"TypeF")==False):
        ns=errordict[5]+"for"+str(l1[0])
        return ns
    else:
        return True
#---HANDLE VARIABLES AND LABELS ERRORS----
def handle_variables(l1,ln):
    if l1[0]=="var" and len(l1)!=2:
        print(str(ln)+":"+"Invalid syntax for variable declaration")
        return
    if l1[0]=="var":
        if l1[1] in vard:
            print(str(ln)+":"+"Multiple definition of variables")
            return
        else:
            vard[l1[1]]=ln
    return 

def handle_labels(l1,ln):
    if(l1[0][-1]==":"):
        if(l1[0][0:-1] in labeld):
            print(str(ln)+":"+"Multiple declaration of labels")
            return False
        else:
            labeld[l1[0][0:-1]]=ln
    return True
#----MAIN LOOP FOR GENERATION OF ERRORS AND PRODUCING BINARY CODE----
getb= lambda x, n: format(x, 'b').zfill(n)
def TypeA(l,ln): 
    A={"add":"10000","sub":"10001","mul":"10110","xor":"11010","or":"11011","and":"11100"}
    un="00"
    nd=typeAerr(l)
    if nd==True:
        ns=A[l[0]]+un+getb(int(l[1][1]),3)+getb(int(l[2][1]),3)+getb(int(l[3][1]),3)
        return ns+"\n"
    else:
        return str(ln)+":"+nd

def TypeB(l,ln): 
    TypeB={"mov":"10010","rs":"11000","ls":"11001"}
    reg1s=getb(int(l[1][1]),3)
    nd=typeBerr(l)
    
    if nd==True:
        ns=TypeB[l[0]]+reg1s+getb(int(l[2][1:]),8)
        return ns+"\n"
    else:
        return str(ln)+":"+nd

def TypeC(l,ln): 
    TypeC={"div":"10111","mov":"10100","not":"11101","cmp":"11110"}
    nd=typeCerr(l)
    if nd==True:
        reg1s=getb(int(l[1][1]),3)
        reg2s=getb(int(l[2][1]),3)
        ns=TypeC[l[0]]+"00000"+reg1s+reg2s
        return ns+"\n"
    else:
        return str(ln)+":"+nd

def TypeD(l,ln): 
    TypeD={"ld":"10100","st":"10101"}
    reg1s=getb(int(l[1][1]),3)
    nd=typeDerr(l)
    if nd==True:
        ns=TypeD[l[0]]+reg1s+vard[l[2]]
        return ns+"\n"
    else:
        return str(ln)+":"+nd

def TypeE(l,ln): 
    TypeE={"jmp":"11111","jlt":"01100","jgt":"01101","je":"01111"}
    nd=typeEerr(l)
    if nd==True:
        ns=TypeE[l[0]]+"000"+l[1]
        return ns+"\n"
    else:
        return str(ln)+":"+nd
#----LIST CONTAINING DIFFERENT OPERATIONS-----
Lta=["add","sub","mul","xor","or","and"]
Ltb=["mov","rs","ls"]
Ltc=["div","mov","not","cmp"]
Ltd=["ld","st"]
Lte=["jmp","jlt","jgt","je"]
L=["add","sub","mul","xor","or","and","mov","rs","ls","div","mov","not","cmp","ld","st","jmp","jlt","jgt","je"]
#-----MAIN CHECK FUNCTION FOR PRINTING THE BINARY CODE ------
def check(l,ln):
    if l[0] in Lta:
        print(TypeA(l,ln))
    elif l[0] in Ltb :
        if l[0]!="mov":
            print(TypeB(l,ln))
        elif l[0]=="mov" and l[2][0]=="$":
            print(TypeB(l,ln))
    if l[0] in Ltc:
        if l[0]!="mov":
            print(TypeC(l,ln))
        elif l[0]=="mov" and l[2][0]=="R":
            print(TypeC(l,ln))
    elif l[0] in Ltd:
        print(TypeD(l,ln))
    
    elif l[0] in Lte:
        print(TypeE(l,ln))
#---MAIN FUNCTION TO CALL THE CHECK FUNCTION----
flag=0
flag1=0
ln=1                                         
for i in l1:
    s=i.split()
    if (s==[]):
        pass
    elif (s[0]=="var" and flag!=1):
        handle_variables(s,ln)
    elif (s[0]=="var" and flag==1):
        handle_variables(s,ln)
        print(str(ln)+":"+errordict[13])
    elif s[0] in L:
        flag=1
        check(s, ln)
    elif s[0][-1]==":":
        flag=1
        if (s[1:]==[]):
            print(str(ln)+"Invalid declaration of label")
        elif (handle_labels(s,ln)==False):
            pass
        else:
            s.pop(0)
            check(s,ln)
    elif s[0] =="hlt":
        flag1=1
        print("0101000000000000")
        break
    else:
        print(str(ln)+"Neither a label nor a variable nor an instruction")
    ln+=1
if (ln==len(l1) and "hlt" not in labeld and flag1!=1) :
    print("hlt not present in the code")

#----END -----

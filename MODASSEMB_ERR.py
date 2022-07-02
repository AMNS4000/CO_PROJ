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
vard=[]
labeld=["hlt"]
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
           12:"undefined label"}
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
    if (l1[2] in labeld):
        return False
    else:
        return True
def checkuseofvariable(l1):
    if (l1[2] not in vard):
        return False
    else:
        return True
def checkuseoflabels(l1):
    if (l1[2] not in labeld):
        return False
    else:
        return True
def checkuseofvariablesinplabels(l1):
    if (l1[2] in vard):
        return False
    else:
        return True
def typeA(l1):
    if (checklengthofInstuct(l1,"TypeA")==False):
        ns=errordict[5]+"for"+str(l1[1])
        return ns
    elif (useofFLAGS(l1)==False):
        return errordict[7]
    elif (checkcorrectregister(l1,"TypeA")):
        return "register"+str(l1[checkcorrectregister(11,"TypeA")])+"does not exist and is invalid"
    else:
        return True
def typeB(l1):
    if (checklengthofInstuct(l1,"TypeB")==False):
        ns=errordict[5]+"for"+str(l1[1])
        return ns
    elif (useofFLAGS(l1)==False):
        return errordict[7]
    elif (checkcorrectregister(l1,"TypeB")):
        return "register"+str(l1[1])+"does not exist and is invalid"
    elif (checkdollar(l1[2][0])==False):
        return errordict[8]
    elif (checkimmediatevalue(l1[1:])==False):
        return errordict[1]
    else:
        return True
def typeC(l1):
    if (checklengthofInstuct(l1,"TypeC")==False):
        ns=errordict[5]+"for"+str(l1[1])
        return ns
    elif (useofFLAGS(l1)==False):
        return errordict[7]
    elif (checkcorrectregister(l1,"TypeC")):
        return "register"+str(l1[1])+"does not exist and is invalid"
    elif (l1[1]=="mov"):
        l2=l1[1:]
        if (checkcorrectregister(l2)==False):
            return "register"+str(l1[2])+"does not exist and is invalid"
    else:
        return True
def typeD(l1):
    if (checklengthofInstuct(l1,"TypeD")==False):
        ns=errordict[5]+"for"+str(l1[1])
        return ns
    elif (checkuseoflabelsinpvariables(l1)==False):
        return errordict[2]
    elif (checkuseofvariable(l1)==False):
        return errordict[6]
    else:
        return True
def typeE(l1):
    if (checklengthofInstuct(l1,"TypeE")==False):
        ns=errordict[5]+"for"+str(l1[1])
        return ns
    elif (checkuseofvariablesinplabels(l1)==False):
        return errordict[11]
    elif (checkuseoflabels(l1)==False):
        return errordict[12]
    else:
        return True
def typeF(l1):
    if (checklengthofInstuct(l1,"TypeF")==False):
        ns=errordict[5]+"for"+str(l1[1])
        return ns
    else:
        return True

    



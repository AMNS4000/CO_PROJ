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
    if (l1[2] not in vard):
        return False
    else:
        return True



from math import *
from math import ceil
from math import log

"""Digital Logic Gates"""

def NOT(x):
    if x==0:
        return(1)
    else:
        return(0)

def AND(x,y):
    if x==1 and y==1:
        return(1)
    else:
        return(0)

def OR(x,y):
    if x==1 or y==1:
        return(1)
    else:
        return(0)

def XOR(x,y):
    if x==y:
        return(0)
    else:
        return(1)

"""Intenger to String converter"""

def int_to_string(x):
    x=s=[(x//(10**j))%10 for j in range(ceil(log(x+1, 10))-1, -1, -1)]
    return(x)

"""I/O solutions"""

def decimal_to_binary(x):
    l = []
    s = []
    while x>0:
        l.append(x%2)
        x=x//2
    for i in range(1,len(l)+1,1):
        s.append(l[len(l)-i])
    return(s)

def binary_to_decimal(x):
    s=int_to_string(x)
    x=0
    for i in range(1,len(s)+1,1):
        x=x+(2**(i-1))*s[len(s)-i]
    return(x)

"""Processor: Functions from digital logic gates"""

def half_adder(x,y):
    s=XOR(x,y)
    Cout=AND(x,y)
    print(s)
    return(s,Cout)

def full_adder(x,y,Cin):
    s=XOR(XOR(x,y),Cin)
    Cout=OR(AND(x,y),AND(XOR(x,y),AND(Cin,XOR(x,y))))
    print(s)
    return(s,Cout)

"""For any number of bits"""

#Enter x and y as arrays

#Sum of 8 bits

def addition_binaryIO(X,Y):
    if len(X)!=8:
        print('Input 8 bits!')
    S=[]
    s,Cin=half_adder(X[0],Y[0]) #Initialisation: sum of the first two bits
    S.append(s)
    for j in range(1,len(X)): #Sum of the subsequent bits
        s,Cin=full_adder(X[j],Y[j],Cin)
        S.append(s)
    if Cin==1:
        print('Overflow')
    return(S)

def addition_decimalIO(x,y):
    X=decimal_to_binary(x)
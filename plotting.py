#!/usr/bin/env python

import sys

moteId=[1,2,3,4,5]
hexList =[1,2]
X_values=[]
Y_values=[]
Z_values=[]

def paddedHex ( number ):
    return "{0:#0{1}x}".format(int(number),4);


def toHex( asciiList ):    
    for i in range(0,len(asciiList)-1):
        #hexList.append(hex(int(asciiList[i]))+hex(int(asciiList[i+1]))[2:])
        #print asciiList[i]+asciiList[i+1]
	hexList.append(paddedHex(asciiList[i])+paddedHex(asciiList[i+1])[2:])
        i+=2
	
    return

def toInt ( hList ):
    for i in range(0,len(hList)):
	hList[i]=int(str(hList[i]),16)
    return

def arrangeValues( numList):
    for i in range(0,len(numList)):
        X_values.append(numList[i])
	Y_values.append(numList[i+1])
	Z_values.append(numList[i+2])
        i+=3
return




for line in sys.stdin:
    data = line.split('-')
    
    toHex(data)
    toInt(hexList)
    #print hexList
    #print int(str(hexList[0]),16)
    #print hexList[0]
    arrangeValues(hexList)
    hexList=[]
    
     
    
   
    
        
    

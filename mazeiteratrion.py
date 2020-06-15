# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:21:51 2020

@author: Paddy
"""

from random import randrange

tried=0
works=0


#  original Magic Table. 2 for Random
mysteryTable={
    "00000":1,
    "00001":1,
    "00010":1,
    "00011":2,
    "00100":0,
    "00101":0,
    "00110":2,
    "00111":2,
    "01000":1,
    "01001":1,
    "01010":1,
    "01011":1,
    "01100":2,
    "01101":0,
    "01110":0,
    "01111":0,
    "10000":1,
    "10001":1,
    "10010":1,
    "10011":2,
    "10100":0,
    "10101":0,
    "10110":0,
    "10111":0,
    "11000":2,
    "11001":0,
    "11010":1,
    "11011":2,
    "11100":2,
    "11101":0,
    "11110":0,
    "11111":0,
    }



# mysteryTable={
#     "00000":0,
#     "00001":0,
#     "00010":0,
#     "00011":0,
#     "00100":0,
#     "00101":0,
#     "00110":0,
#     "00111":0,
#     "01000":0,
#     "01001":0,
#     "01010":0,
#     "01011":0,
#     "01100":0,
#     "01101":0,
#     "01110":0,
#     "01111":0,
#     "10000":0,
#     "10001":0,
#     "10010":0,
#     "10011":0,
#     "10100":0,
#     "10101":0,
#     "10110":0,
#     "10111":0,
#     "11000":0,
#     "11001":0,
#     "11010":0,
#     "11011":0,
#     "11100":0,
#     "11101":0,
#     "11110":0,
#     "11111":0,
#     }


def get_nth_key(dictionary, n=0):
    if n < 0:
        n += len(dictionary)
    for i, key in enumerate(dictionary.keys()):
        if i == n:
            return key
    raise IndexError("dictionary index out of range") 



index=0







    

def checkMaze(table):
        global tried
        global works
        
        tried=tried+1
        mysteryTable=table
        
        #Initialize first row
        A=[[1,0,0,0,1,1,0,0,0,1]]
        
        #create maze range is number of rows. 
        for i in range(1000):
            #initialize new row
            newRow=[1,0]
            while len(newRow) < 9:
                #set values to table up
                a=newRow[len(newRow)-2]
                b=newRow[len(newRow)-1]
                c=A[len(A)-1][len(newRow)-1]
                d=A[len(A)-1][len(newRow)]
                e=A[len(A)-1][len(newRow)+1]
                
                
                find=str(a)+str(b)+str(c)+str(d)+str(e)
                #look up table
                newValue=mysteryTable[find]
                #if table delivers a 2 find 0 or 1 randome
                if newValue==2:
                    newValue=randrange(2)
                    
                #add found value to row. 
                newRow.append(newValue)
            #initialize last value from row which is needed for next row caluclation
            newRow.append(1)
            #Append calculated row to maze.
            A.append(newRow)   
            
        #Since second row is a wall we cann fill it up with 1
        for i in range(len(A)):
            A[i][1]=1
        #set possible player paths in first row. 
        A[0]=[1,5,5,5,1,1,5,5,5,1]
        
        moved=True
        
        #Travers the whole maze top to bottom
        for i in range(len(A)-1):
            #check every field
            for j in range(len(A[i])):
                # If a field is free and the field above has a player. Place player in field as 5.
                #moving down is only way to get to the next row. 
                if A[i][j]==0 and A[i-1][j] == 5:
                    A[i][j]=5
            #move all players if possible
            while moved:
                moved=False
                #players can move left and right inside one row. 
                #For every player make every possible move.
                for j in range(len(A[i])):
                    if A[i][j]==5 and A[i][j+1]==0:
                        moved=True
                        A[i][j+1]=5
                    if A[i][j]==5 and A[i][j-1]==0:
                        moved=True
                        A[i][j-1]=5
            moved=True
        
        
        
        pathfound=True
        
        #Look for the point were the last path broke of if it exists. 
        for i in range(len(A)):
            if not 5 in A[i]:
                if i < len(A)-1:
                    # print("Break found ")
                    # print("Row: " + str(i))
                    # print(A[i-1])
                    # print(A[i])
                    # print(A[i+1])
                    pathfound=False
                    break
                    
               
        # if path was found print it so people can see it. 
        #row=''
        if pathfound:
            
            works=works+1
            # for i in range(len(A)):
            #     for j in range(len(A[i])):
            #         if A[i][j]!=5:
            #             row=row+'|'
            #         else:
            #             row=row + "X"
            #         row=row+'  '
            #     print(row)
            #     row=''
        if tried%1000==0:
           print("Tried: " + str(tried)+ " Works: " + str(works))

def recursionfuckery(table,index):
    for i in (0,1,2):
        key=get_nth_key(table,index)
        if i<table[key]:
            continue
        table[key]=i
        if index+1<len(table):
            table=recursionfuckery(table,index+1)
        else:
            checkMaze(table)
                
    return table

recursionfuckery(mysteryTable, index)


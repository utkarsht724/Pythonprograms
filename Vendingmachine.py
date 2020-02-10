#program to find minimum no of Notes as well as the Notes to be returned by the Vending Machine
from array import *
amount=int(input("enter the amount"))      #taking input amount from user
a=array('i',[2000,500,200,100,50,10,5,2,1])
count=0
for i in range(len(a)):                    #iterartes till length of array
    while a[i]<=amount:                     #iterates until the amount is more than or equal to given notes
         amount = amount-a[i]
         count += 1                          #counts the no of notes

    if count!= 0:
     print(a[i],"k",count)
     count=0





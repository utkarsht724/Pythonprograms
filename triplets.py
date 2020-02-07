#program to find triplet which sum is equal to zero

from array import *
arr = array('i',[])
arr_length=int(input("enter the length of array "))       #taking length of array from user

for e in range(arr_length):                                      #iterate till input length size
    x=int(input("enter the next element of array :"))            #taking input from user
    arr.append(x)
for f in range(0,arr_length-2):                           #iterates n-2 times from  arr[0] to length-2
    for d in range(f+1,arr_length-1):                     #iterates n-1 times from arr[1] to length-1
        for q in range(d+1,arr_length):                   #iterates n times from  arr[2] to length
            if arr[f]+arr[d]+arr[q]==0:
                print("the triplet is: FOUND")
                print(arr[f],arr[d],arr[q])

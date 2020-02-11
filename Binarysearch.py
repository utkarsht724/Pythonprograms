from array import *
def binarySearch(arr,x):
    l=0
    r=len(arr)
    while(l<=r):
       m=l+((r-l)/2)
       res=(x==arr[m])
       if res==0:
         return m-1
         print("element found")
       elif res>0:
          l=m+1
    else:
       r=m-1
       return -1


arr=["utkarsh","ananya","shambhavi","ashu"]
x=input("enter the word u want to search")
result = binary search(arr,x)
if(result==-1)
    print("element is not present")
else
    print("element found",result)

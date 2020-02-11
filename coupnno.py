#Given N distinct Coupon Numbers, how many random numbers do you need to generate distinct coupon number?
import random
count=0
limit=int(input("enter a range you want to generate the coupon"))   #taking input(limit) from the user
for i in range(limit):                                               #iterates until input limit
    first_random_no=random.uniform(1,3)                              #generate first random no
    second_random_no=random.uniform(1,3)
    if first_random_no!=second_random_no:                            #check whether its a new one
        count+=1
        print(count, second_random_no,":this one is new coupon")

#power of 2 to less than or equal to 2**n

n =int(input("enter the value"))

#to take input from the user

for i in range(1,2**n):       #iterates 2**n times from i = 1 to 2**n
 print("2**", i, "=", 2**i)


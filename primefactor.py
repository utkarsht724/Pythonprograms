#program to find the prime factor

number=int(input("enter the number"))   #taking input from the user

for i in range(2,number):              #iterates outer loop from 2 to input number
   while number%i==0:                   #inner loop run until condition is true
     print(i)
     number=number/i                    #check the factor of a input no
i += 1                                   #increment the value of i after completion of inner loop

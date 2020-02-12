#program to display nth harmonic value

def Harmonic(Nth):
 harmonic_no=1.00
 for number in range (2,Nth+1):   #iterate Nth+1 times from 2
    harmonic_no += 1/number
    print(harmonic_no)

#driver_code
Nth=int(input("enter the Nth term"))    #to take Nth term from the user
print(Harmonic(Nth))
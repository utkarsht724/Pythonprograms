#temperature conversion into fahrenhite

def fahrenhite_conversion(C):
 try:
    return C*(9/5) + 32
 except:
   print("there is error in program")
def celcius_conversion(F):
   return  F-32*(5/9)

#driver codes

t_celcius=int(input("enter the temprature in celcius: "))
print("temperature in fahrenhite: ",fahrenhite_conversion(t_celcius))
print()
t_fahrenhite=int(input("enter the temprature in fahrenhite: "))
print("temperature in celcius: ",celcius_conversion(t_fahrenhite))





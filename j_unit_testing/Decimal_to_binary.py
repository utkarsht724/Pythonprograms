def Decimal_to_bnary(number):
  if number >0:
      Decimal_to_bnary(number//2)
  print(number%2,end=" ")
def
number=int(input("enter the number"))
Decimal_to_bnary(number)


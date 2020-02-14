#program to find monthly payment
def Monthly_Payment(P,Y,R):
  Principle=0
  n=12*Y
  r=R/(12*100)
  try:
     payment= ("the monthly payment is",P*r / 1-(1+r**(-n)))
     print(payment)
  except:
      print("there is error in program")

#driver code
P=int(input("Enter the principle amount"))
Y=int(input("Enter the year"))
R=int(input("Enter the Rate of interest"))
Monthly_Payment(P,Y,R)

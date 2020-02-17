#program to find prime no between 0 to 1000

class prime_no_in_range:
 try:

  def primeno(prime):
      lower = 0
      upper = 1000
      for number in range(lower,upper+1):
          if number>1:
              for i in range(2,number):
                  if number%i==0:
                     break
              else:
                print (number)

 except Exception as e:
    print("TypeError=",type(e))

prime=prime_no_in_range()
prime_no_in_range.primeno(prime)



#program to find wind chill

import math
t=int(input("enter the temperarture in fahreanhite"))                #taking temperature from user
v=int(input("enter the wind speed in miles per hour="))              #taking wind speed from user
w= 35.74 + 0.6215*t + (0.4275*t - 35.75) * math.pow(v,0.16)         #find wind chill using formula
print("the wind chill is :",w)




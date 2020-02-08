#program to replace USERNAME  with any name in a string

import re
str= print("Hello USERNAME How are you?")
name=input("Enter the name you want to replace with USERNAME  :")  #taking input name from the user
str ="Hello USERNAME How are you?"
regex =re.compile("USERNAME")
str = regex.sub(name,str)               #replace Username with input name by using regular expression
print(str)

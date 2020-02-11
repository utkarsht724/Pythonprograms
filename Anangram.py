#To check two strings are anagram or not
def word_check(first_string,second_string):
 if sorted(first_string)==sorted(second_string):        #check sorted string
   print("this is anangram")
 else:
    print("hey user try again")

#driver_code
first_string = input("enter the first string")
second_string = input("enter the second string")
word_check(first_string,second_string)
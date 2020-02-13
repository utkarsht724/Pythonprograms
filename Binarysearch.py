#binary search the word from word list

def binary_search( a_list,key):
  try:
    low = 0
    high = len(a_list) - 1
    found = False
    while(low <= high and not found ):
      midpoint = (low + high) // 2
      if a_list[midpoint] == key:
        found = True
      elif key < a_list[midpoint]:
           high = midpoint - 1
      else:
          low = midpoint + 1
  except:
      print("there is something wrong in your program")
  finally:
    return found


a_list = input("enter the names in the list").split()
print(sorted(a_list))
key = input("enter the word you want to search")
print(binary_search(a_list,key))

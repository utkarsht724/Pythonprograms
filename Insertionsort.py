#sort the string using insertion sort
def insertion_sort(names):
    for i in range(1,len(names)):
        value=names[i]                                #select value to be inserted
        hole=i
        while hole>0 and names[hole-1]>value:         #locate hole position for the element to be inserted
         names[hole]=names[hole-1]
         hole-=1
        names[hole]=value                             #insert the element at hole position

#driver_class
names = input("enter the name u want to sort: ").split()
insertion_sort(names)
print(names)
import random

head = 0
tail = 0
flip = int(input("how many time you want to flip a coin"))
for i in range(flip):
    toss = random.uniform(0,1)
    if toss > 0.5:
      print("Heads")
      head += 1
    else:
      print("Tail")
      tail += 1


print("Heads:",head)
print("Tails:",tail)

head_percentage= head/(head + tail)*100
tail_percentage= tail/(head+tail)*100
print("the percentage of head:",head_percentage)
print("the percentage of tail:",tail_percentage)

# Simulates a gambler who start with $stake and place fair $1 bets until he/she goes broke or reach goal.
import random
win=0
count=0
loss=0
goal=int(input("enter the no you want to play"))  #taking input (no of times he want play)
stake=int(input("enter the stake you have"))      #taking input (no of stakes he have for bet)
while stake!=0 and goal!=0:                       #iterates until stake and goal !=0
        bet =random.randint(0,1)
        if bet==0:
             loss+=1
             stake-=1
             count+=1

        if bet==1:
            win+=1
            stake+=1
            count+=1
        goal -=1
if(count!=0):
 print("the no of time he/she win:",win)
 print("the percentage of win",(win / count ) * 100 )
 print("the percentage of loss",(loss / count ) * 100)


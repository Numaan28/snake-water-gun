import random
'''
snake 1
water -1
gun 0
'''
print("Welcome to Snake-Water-Gun Game!")
print("\nGame Rules:")
print("-> Snake drinks Water: Snake wins")
print("-> Water douses Gun: Water wins")
print("-> Gun kills Snake: Gun wins\n")
print("choose s for snake, g for gun, w for water")
computer = random.choice([1, -1, 0])
youstr = input("enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "snake", -1: "water", 0: "gun"}

you = youDict[youstr]

print(f"you choose {reverseDict[you]} computer choose {reverseDict[computer]}")

if(computer==you):
    print("its a draw")

else:
    if(computer ==1 and you == -1):
        print("you loose")

    elif(computer ==-1 and you == 1):
        print("you win")

    elif(computer ==0 and you ==1):
        print("you loose")

    elif(computer ==1 and you ==0):
        print("you win") 

    elif(computer ==-1 and you ==0):
        print("you loose")

    elif(computer ==0 and you ==-1):
        print("you win")

    else:
        print("something went wrong")


#code by salman 
# github = numaan28          

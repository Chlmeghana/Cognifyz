import random 
def guess(a,x):
    if(a==x):
        print("Your guess is right")#if user guess and program generated no. is same
        return 1
    elif(x>a):
        print("Your guess is too high")#if user guess is greater than the program generated no. 
        return 0
    else:
        print("Your guess is too low")#if user guess is less than the program generated no.
        return 0
a=random.randint(1,100)#This function stores a random number between the arguments 1 and 100
c=0
while True:
    x=int(input("Type your guess between 1 and 100: "))#Take a guess from the user untill he gets it right
    if(x>100 or x<1):
        print("Try again")
    else:
        c=guess(a,x)
        if c==1:
            break
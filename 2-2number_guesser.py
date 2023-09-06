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
p=int(input("Enter the lowest range: "))#Take the range from user that is lower limit 
q=int(input("Enter the highest range: "))#Take the range from user that is upper limit
a=random.randint(p,q)
c=0
while True:
    x=int(input("Type your guess between {0} and {1}: ".format(p,q)))#Take a guess from the user untill he gets it right
    if(x>q or x<p):
        print("Try again")
    else:
        c=guess(a,x)
        if c==1:
            break
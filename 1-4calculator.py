def calculator(a,b,n):
    if(n==1):
        return "a+b={}".format(a+b)
    elif n==2:
        return "a-b={}".format(a-b) 
    elif n==3:
        return "a*b={}".format(a*b) 
    elif n==4:
        return "a/b={}".format(f'{(a/b):.2f}')#syntax used to get float value rounded by 2 digits
    elif n==5:
        return "a%b={}".format(a%b)
    else:
        return "invalid"
a=float(input("Enter first number: "))#Take 1st number input from user
b=float(input("Enter second number: "))#Take 2nd number input from user
n=float(input("Type \n1 to perform addition \n2 to perform subtraction \n3 to perform multiplication \n4 to perform division \n5 to perform modulo\n")) 
print(calculator(a,b,n))   
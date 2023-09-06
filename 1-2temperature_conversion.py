def toCel(n):
    return (n-32)*(5/9)#Formula for converting Fahrenheit value to Celsius value
def toFah(n):
    return (n*(9/5))+32#Formula for converting Celsius value to Fahrenheit value
a=int(input("Input the Temperature value: "))
b=int(input("Type 1 if given value is in Celsius,Type 2 if given value is in Fahrenheit "))
if b==1:
    print("Celsius=",a,'\n Fahrenheit=',f'{toFah(a):.2f}')#syntax used to get float value rounded by 2 digits
else:
    print("Fahrenheit=",a,'\n Celsius=',f'{toCel(a):.2f}')#syntax used to get float value rounded by 2 digits
def strength_checker(s):
    p="!@#$%^&*()_+-={'}|[]\:"";'<>?,./"
    if len(s)<8:#A strong password length should be atleast 8 characters
        print("Too weak!,Length should be atleast 8 characters")
        return 0
    elif not any(i.isupper() for i in s):#A strong password should contain atleast 1 uppercase letter in it
        print("Too weak!,Password should contain uppercase letters")
        return 0
    elif not any(i.islower() for i in s):#A strong password should contain atleast 1 lowercase letter in it
        print("Too weak!,Password should contain lowercase letters")
        return 0
    elif not any(i.isdigit() for i in s):#A strong password should contain atleast 1 digit in it
        print("Too weak,Password should contain digits")
        return 0
    elif not any(i in p for i in s):#A strong password should contain atleast 1 special character in it
        print("Too weak,Password should contain special characters")
        return 0
    else:
        print( "Your Password is Strong")
        return 1
        
while True:
    s=input("Enter Password: ")#Take input string from user that is a password
    c=strength_checker(s)#invoke the strength_checker function
    if(c==1):#indicates whether the entered password is strong or whether the user need to retry
        break 
    else:
        print("Try Again!")

    

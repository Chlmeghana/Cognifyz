def palindrome(s):
    p=s.lower()
    x=p[::-1]#syntax used to reverse the given string
    if x==p:#to check palindrome,we need to verify if the original string and its reverse string is equal or not
        print(s+" is a palindrome")
    else:
        print(s+" is not a palindrome")
s=input("Enter a String: ")#Take a input string from user
palindrome(s)
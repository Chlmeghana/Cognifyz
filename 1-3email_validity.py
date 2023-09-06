import socket
import re
def email_validity(s):
    pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$'#this is a valid regular expression pattern of a mail adress,in which '@','.' are mandatory
    if re.match(pattern,s) != None:#used to check if pattern,string s matches or not
        domain=s.split('@')[1]#used to get domain of mail string s i.e. string present after '@'
        try:
            socket.gethostbyname(domain)#used to check if domain exists or not,this is done by reesolving the domain to its respective IP adress.
            return True 
        except socket.gaierror: #if try throws an error that means the domain is not valid so,it returns false.
            return False 
    return False
s=input("Enter A mail adress: ")#Take input mail adress from user
l=s.lower()#since if a mail adress contains any uppercase letters, it is considered as invalid
if(l!=s):
    print("invalid mail")
else:
    if email_validity(s):
        print("valid mail")
    else:
        print("invalid mail")
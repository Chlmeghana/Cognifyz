def fibno(l,a,b,n):
    c=a+b 
    l.append(c)
    x=len(l)
    if x<n:#used to check the length of the sequence untill the length the user has prompted this statement gets executed.
        return fibno(l,l[x-2],l[x-1],n)
    else:
        return l 
n=int(input("Enter the length of fibnocci sequence: "))#Take input from user,the length of the fibnocci sequence
if(n==1):#the 1st element in a fibnocci sequence is 0
    print(0)
elif(n==2):#the 1st,2nd elements in a fibnocci sequence is 0,1
    print(0,1)
else:
    l=[0,1]
    l=fibno(l,l[0],l[1],n)
    print(*l)




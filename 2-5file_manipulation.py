def count_words(user_file):
    c={}#dictionary that contains each word in the file and the no. of its occurences
    with open(user_file,"r") as file:#we open the file with the object "file",and we perform only read action so do only read action "r"
        for i in file:#i contains lines in a file,in the first execution of the loop,i contains the first line of the file.
            words=i.split()
            for j in words:#j contains each word in a line which are stored in words list,in the first execution of the loop,j contains the first word of the list.
                j=j.lower()
                if j in c:#counts the occurences
                    c[j]+=1
                else:
                    c[j]=1
    sc=sorted(c.items())
    for i,j in sc:
        print(f"{i}:{j}")
user_file="2-5File_manipulation.txt"#name of the file hich i wanted to read,we can also ask the user to enter his file name
count_words(user_file)

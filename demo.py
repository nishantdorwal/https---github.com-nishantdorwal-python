  
data={"user":["user1","user2","user3","user4"],"password":[111,222,333,444]}
user1=input("enter the user name")
p=''
if user1 in data['user']:
    pas=int(input("enter the password"))
    for i in range(len(data["user"])):
        if(user1==data["user"][i]):
            p=i
            break
    if pas==data["password"][p]:
        print("Login")  
    else:
        print("enter correct password")    
else:
    print ("enter corect username")    

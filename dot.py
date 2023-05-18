product=["product1","product2","product3","product4"]
rate =[100,200,240,233]
qty=[20,32,20,40]
addproduct=[]
addqty=[]
addrate=[]
user  = ["user1","user2"]
password=[111,123]
username = input("enter name")
if username in user:
     print("user login")
p=''
r=False
for i in range(len(user)):
    if(username == user[i]):
        r=True
        p=i
        break
print(p)
log= False
if(r):
    password1 =int( input("Enter password"))
    if password1==password[p]:
        print("login")
        log=True
else:
    print("not login")
p_pos=-1
p_find=False
if(log):
    i=0
    while(i<len(product)):
        print(product[i],end="\t")
        print(rate[i],end="\t")
        print(qty[i],end="\n")
        i=i+1
    while True:
        ch = input("enter 'y' to add product ")
        if(ch == 'y'):
            pro=input("enter product name")
            for i in range(len(product)):
                if(pro==product[i]):
                    p_pos=i
                    p_find=True
                    break
                
            if p_find:
                q_pos=0
                q= int(input("enter qty"))
                if(q<=qty[p_pos]):
                    print(rate[p_pos])
                    if pro not in  addproduct:
                        addproduct.append(pro)
                        addqty.append(q)   
                    else:                  
                        for i in range(len(addproduct)):
                            if(pro==product[i]):
                                q_pos=i
                                addqty[i]=addqty[i]+q
                        continue    
                        
                    addrate.append(rate[p_pos])
                    qty[p_pos]=qty[p_pos]-q                                     
                else:
                    print("you have cross the qty limit") 
        else:
            break
    print("*********** add to cart ************")
    for i in range(len(addproduct)):
        print(addproduct[i],end="\t")
        print(addqty[i],end="\t")
        print(addrate[i],end="\n")
    print("*********** add to cart ************")
    while True:
        rm=input(" product  remove 'y'")
        if rm =='y':
            p=input("enter product name")
            q1=int(input("enter the qty of product"))
            for i in range(len(addproduct)):
                if p==addproduct[i]:
                    addqty[i]=addqty[i]-q1
                        
                    if addqty[i] == 0:
                        addproduct.pop(i)
                        
        else:
            break            
           
                

    totalpay=0
    for i in range(len(addproduct)):
        print(addproduct[i],end="\t")
        print(addqty[i],end="\t")
        print(addrate[i],end="\n")
        totalpay+=addqty[i]*addrate[i];
    print("Total pay",totalpay)
    pay =int(input("enter pay"))
    if(pay==totalpay):
        print("thx")
    
print("*****************")

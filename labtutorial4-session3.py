
user =["Chen","admin","tom","sammer","shah","keo","jules"] 
userNew=[""]
for i in range(1,7):
 if not user:
    print("You are not the part of user")
 elif user[i]=="admin":
    print(f"Hello {user[i]} \fwould you like to see a status report?")
 else :
    print(f"Hello {user[i]}  \fthank you for logging in again.")
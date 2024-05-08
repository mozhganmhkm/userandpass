username = "mozhgan"
password = "1375mhkm"

username1 = str(input("please enter username:  "))
if username1 == username:
 
   password1 = (input("please enter password:  "))
   if password1 == password:
    print("welcome" + " " + username + ".")
   else:
    print(" password invalid!")

elif username1 != username :
    
    print("user not found!")





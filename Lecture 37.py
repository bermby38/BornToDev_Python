usernameInput = input("Username : ")
passwordInput = input("Password : ")

if usernameInput == "admin":
    if passwordInput == "1234":
        print("Done !!")
    else:
        print("Password Wrong!!")
else:
    print("Username Wrong!!")
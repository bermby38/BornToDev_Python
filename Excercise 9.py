usernameInput = input("Username : ")
passwordInput = input("Password : ")
loginCount = 0

while usernameInput != "admin" or passwordInput != "1234":
    loginCount += 1

    if loginCount <= 2:
        print("----------------------------")
        print("Username or Password Wrong !")
        print("Login attempts = ", loginCount)
        usernameInput = input("Username : ")
        passwordInput = input("Password : ")
    else:
        print("Login exceed limits")
        break

if loginCount < 3:
    print("----------------------------")
    print("Login Success")
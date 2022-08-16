def access():
    text = int(input('''
                1) Register
                2) Login
                3) Forgot Password
                Enter 1, 2 or 3:'''))

    if text == 1:
        register()
    elif text == 2:
        login()
    elif text == 3:
        forgot_password()


def register():
    db = open("database.txt", "r")
    UserName = input("Create Username:")
    Password = input("Create Password:")
    Password1 = input("Confirm Password:")
    count = 0
    count1 = 0
    count2 = 0
    count3 = 0
    str1 = Password
    lis = UserName.split("@")
    lis1 = UserName.split(".")
    u = []
    p = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        u.append(a)
        p.append(b)
        data = dict(zip(u, p))
    if len(UserName)<=1 or len(Password)<=1:
        print("Incorrect username or password. Please choose forgot password or register")
        access()
    if lis[1].startswith('.'):
        print('''Invalid USername, cannot have '@' and '.' together''')
        register()
    elif lis1[0].endswith('@'):
        print('''Invalid USername, cannot have '@' and '.' together''')
        register()
    elif UserName[0].isdigit():
        print("Username Invalid, cannot start with number.")
        register()
    elif UserName.startswith(('!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '~', '<', ',', '>', '.', '?', '/',
                              '"', "'", ':', ';', '}', ']', '{', '[', '|', '=', '-', '_', '+')):
        print("Username Invalid, cannot start with special character")
        register()
    elif Password != Password1:
        print("Password Do not match, Restart")
        register()
    elif UserName in u:
        print("User already Exists. Try login or Forgot Password")
        access()

    else:
        if len(Password) < 5:
            print("Password too Short. Restart")
            register()
        elif len(Password) > 16:
            print("Password too long. Restart")
            register()
        elif str1 == Password:
            for i in str1:
                if i.isupper():
                    count = count + 1
                if i.islower():
                    count1 += 1
                if i in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '`', '~', '<', ',', '>', '.', '?', '/', '"',
                         "'", ':', ';', '}', ']', '{', '[', '|', '=', '-', '_', '+']:
                    count2 += 1
                if i.isdigit():
                    count3 += 1
            if count >= 1 and count1 >= 1 and count2 >= 1 and count3 >= 1:
                db = open("database.txt", "a")
                db.write(UserName + ", " + Password + "\n")
                print("Success")
            else:
                print('''Password does not match required criteria: 
                                 i.e: must have 1 special character, 1 uppercase,
                                 1 lowercase and 1 number.
                                 Please restart again.''')
                register()

        # elif UserName in db:
        #    print("Username already exists.")
        #    register()


def forgot_password():
    db = open("database.txt", "r")
    u = []
    p = []
    for i in db:
        a, b = i.split(", ")
        b = b.strip()
        u.append(a)
        p.append(b)
    data = dict(zip(u, p))
    input_UserName = input("Enter Username:")
    if input_UserName in u:
        print("Select '1' if you want to show your password.")
        print("Select '2' if you want to reset your password.")
        choice = int(input("1 or 2 : "))
        if choice == 1:
            print(data.get(input_UserName))
        elif choice == 2:
            new_pass = input("Enter a new password:")
            input_Password = data.get(input_UserName)
            with open(r'database.txt', 'r') as file:
                data = file.read()
                data = data.replace(input_Password, new_pass)
            with open(r'database.txt', 'w') as file:
                file.write(data)
            print("Password has been successfully changed.")


def login():
    db = open("database.txt", "r")
    input_UserName = input("Enter Username:")
    input_Password = input("Enter Password:")
    if not len(input_UserName or input_Password) < 1:
        u = []
        p = []
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            u.append(a)
            p.append(b)
        data = dict(zip(u, p))
        if input_UserName not in u:
            print("UserName does not exists. Please register.")
            register()
    try:
        if data[input_UserName]:
            try:
                if input_Password == data[input_UserName]:
                    print("Login Successful")
                    print("Hi " + input_UserName + ". Welcome to Python.")
                else:
                    print("Incorrect username or password. Please choose forgot password or register")
                    access()
            except:
                print("Incorrect username or password. Please choose forgot password or register")
                access()
        else:
            print("Username does not exists.")
            register()
    except:
        print("Login Error.")
access()

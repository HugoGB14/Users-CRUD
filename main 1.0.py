import admin
import os

a = admin.admin("list.json")

def main():
    while True:
        a.load_data()
        alfaOption(a)
        os.system('clear')
        

def show_menu(admin_instance):
    text = ""
    for i in range(len(admin_instance.data)):
        text = text + f"{i+1}:{admin_instance.data[i]['Username']}    "
    print(text)

def show_user_info(admin_instance, id):
    user = admin_instance.data[id]
    print(f"""Username:{user['Username']}
Email:{user['Email']}
Level:{user['Permission_level']}""")
    
def permision_level(admin_instance):
    admins = []
    permissionA = False
    permission = False
    for i in range(len(admin_instance.data)):
        if admin_instance.data[i]['Permission_level'] == "Admin":
            admins.append(i)
    username_admin = input("Admin username: ")
    for i in admins:
        if admin_instance.data[i]['Username'] == username_admin:
            userid = i
            permissionA = True
            break
    if permissionA == False:
        return False
    password = input("Admin Password: ")
    if password == admin_instance.data[userid]['Password']:
        permission = True
    return permission

def modify(admin_instance, id, permission):
    user = admin_instance.data[id]
    if permission:
        username = input(f"Username ({user['Username']}): ")
        if username == "": username = user['Username']
        password = input(f"Password ({user['Password']}): ")
        if password == "": password = user['Password']
        email = input(f"Email ({user['Email']}): ")
        if email == "": email = user['Email']
        level = input(f"Level ({user['Permission_level']}): ")
        if level == "": level = user['Permission_level']

        user_dict = {"Username":username,
        "Email":email,
        "Password":password,
        "Permission_level":level}
        admin_instance.update_user(user['Username'], user_dict)

def alfaOption(admin_instance):
    show_menu(admin_instance)
    userid = input("Elige un numero para ver sus datos y tambien puedes poner palabras clave: ") 
    if key_option(admin_instance, userid) == False:
        show_user_info(admin_instance,int(userid) - 1)
        mod = input("Modificar: ")
        if mod == "Yes": p = permision_level(admin_instance)
        elif mod == "No": p = False
        else: 
            print("Argumento erroneo")
            p = False
        modify(admin_instance, int(userid) - 1, p)

def key_option(admin_instance, key):
    if key == "beta":
        betaOption(admin_instance)
    elif key == "gamma":
        gammaOption(admin_instance)
    elif key == "exit":
        os.system('clear')
        exit(0)
    else: return False
    return True

def add(admin_instance, permission):
    if permission:
        username = input("Username: ")
        password = input("Password: ")
        email = input("Email: ")
        level = input("Level: ")
        user_dict = {"Username":username,
        "Email":email,
        "Password":password,
        "Permission_level":level}
        admin_instance.add_user(user_dict)

def betaOption(admin_instance):
    add(admin_instance, permision_level(admin_instance))

def delete(admin_instance, permission):
    if permission:
        userid = int(input("Eliga el numero que hay arriba para eliminar el usuario al lado del numero:")) - 1
        user = admin_instance.data[userid]
        admin_instance.remove_user(user['Username'])

def gammaOption(admin_instance):
    delete(admin_instance, permision_level(admin_instance))


if __name__ == "__main__":
    main()

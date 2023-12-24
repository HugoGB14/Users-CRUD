import hashlib
import admin
import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')

def main():
    os.system('clear')
    file = input("Ruta del archivo: ")
    a = admin.admin(file)
    while True:
        a.load_data()
        os.system('clear')
        key = input("Introduca una clave para usar su funcion: ")
        if not key_option(a, key):
            print("Se ha introducvido una clave incorrecta")
        
def calcular_hash_sha256(texto):
    return hashlib.sha256(texto.encode()).hexdigest()


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
    if len(admins) == 0: return True
    username_admin = input("Admin username: ")
    for i in admins:
        if admin_instance.data[i]['Username'] == username_admin:
            userid = i
            permissionA = True
            break
    if permissionA == False:
        return False
    password = input("Admin Password: ")
    if calcular_hash_sha256(password) == admin_instance.data[userid]['Password']:
        permission = True
    return permission

def modify(admin_instance, id, permission):
    user = admin_instance.data[id]
    if permission:
        username = input(f"Username ({user['Username']}): ")
        if username == "": username = user['Username']
        password = input(f"Password ({user['Password']}): ")
        if password == "": password = user['Password']
        else: password = calcular_hash_sha256(password)
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
    userid = int(input("Eliga el numero que hay arriba para modificar el usuario al lado del numero: ")) - 1
    modify(admin_instance, int(userid), permision_level(admin_instance))
        

def deltaOption(admin_instance):
    show_menu(admin_instance)
    userid = int(input("Eliga el numero que hay arriba para ver la informacion el usuario al lado del numero: ")) - 1
    show_user_info(admin_instance, userid)
    input("Presione enter para retornar")

def key_option(admin_instance, key):
    if key == "alfa":
        alfaOption(admin_instance)
    elif key == "beta":
        betaOption(admin_instance)
    elif key == "gamma":
        gammaOption(admin_instance)
    elif key == "delta":
        deltaOption(admin_instance)
    elif key == "exit":
        os.system('clear')
        exit(0)
    else: return False
    return True

def add(admin_instance, permission):
    if permission:
        username = input("Username: ")
        password = calcular_hash_sha256(input("Password: "))
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
        show_menu(admin_instance)
        userid = int(input("Eliga el numero que hay arriba para eliminar el usuario al lado del numero: ")) - 1
        user = admin_instance.data[userid]
        admin_instance.remove_user(user['Username'])

def gammaOption(admin_instance):
    delete(admin_instance, permision_level(admin_instance))


if __name__ == "__main__":
    main()

print("////SISTEMA DE CONTROL DE VISITAS MEDICAS///")
employee  =[]
password =[]
while True:
    print("-Eliga una una de las opciones.-")
    print("*1.-Crear cuenta.")
    print("*2.-Ingresar.")
    option = int(input("responda aqui: "))
    if option == 1:
        user =str(input("ingrese su nombre de usuario: "))
        clave =str(input("ingrese su contraseña"))
        if user  not in employee:
            employee.append(user)
            password.append(clave)
        else:
            print("este usuario ya existe ingrese otro")    
    if option == 1:
        user =str(input("ingrese su nombre de usuario: "))
        clave =str(input("ingrese su contraseña"))
        if user in employee and clave in password:
            print("bienvenido al sistema")
        else:
            print("usuario o contraseña incorrecta")    
            break
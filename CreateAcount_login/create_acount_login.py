print("////SISTEMA DE CONTROL DE VISITAS MEDICAS///")
employee  =[]
password =[]
while True:
    print("--Eliga una una de las opciones.--")
    print("*1.-Crear cuenta.")
    print("*2.-Ingresar.")
    print("*3.-Salir. ")
    option = int(input("responda aqui: "))#error si se poone un especio vacio  letras
    if option == 1:
        user = str(input("///Crea tu nombre de usuario: "))
        clave = str(input("///Crea tu contraseña contraseña: "))
        if user not in employee:
            employee.append(user)
            password.append(clave)
            print("///Cuenta creada con exito.")
            print(employee )
            print(password)
        else:
            print("///Este usuario ya existe ingrese otro.")    
    elif option == 2:
        user =str(input("///Ingrese su nombre de usuario: "))
        clave =str(input("///Ingrese su contraseña: "))
        if user in employee:
            lista = employee.index(user)
            if password[lista] == clave:
                print("///Bienvenido al sistema.")
                break #aqui pondre el menu iteractivo despues de pasar el login o creaccion de cuenata
            else:
                print("///Usuario o contraseña incorrecta.") 
        else:
            print("///Este usuario no existe.")           
    elif option == 3:
        print("///Saliendo...")
        break
    else:
        print("///Opcion no valida, intente denuevo.")       
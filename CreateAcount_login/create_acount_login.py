print("////SISTEMA DE CONTROL DE VISITAS MEDICAS///")
employee  =[]
password =[]
while True:
    print("--Eliga una una de las opciones.--")
    print("*1.-Crear cuenta.")
    print("*2.-Ingresar.")
    print("///para salir escriba (SALIR).")
    initial =(input("responda aqui: ")).upper().strip()#error si se poone un especio vacio  letras
    if initial.isdigit(): #usando este metodo para separar valorres str i int
        option = int(initial)
        if option == 1:#condicional para crear cuenta
            user = str(input("///Crea tu nombre de usuario: ")).lower().strip()
            clave = str(input("///Crea tu contraseña contraseña: ")).lower().strip()
            if user not in employee:
                employee.append(user)#metodos para agregar variables a las listas
                password.append(clave)
                print("///Cuenta creada con exito.")
            else:
                print("///Este usuario ya existe ingrese otro.")    
        elif option == 2: #condicional para ingresar 
            user =str(input("///Ingrese su nombre de usuario: ")).lower().strip()
            clave =str(input("///Ingrese su contraseña: ")).lower().strip()
            if user in employee:
                user_1 = employee.index(user)#metodo para buscar su pocicion en la lista 
                if password[user_1] == clave:#comparacion de pociciones en laslistas
                    print("///Bienvenido al sistema.")
                    break #aqui pondre el menu iteractivo despues de pasar el login o creaccion de cuenata
                else:
                    print("///Usuario o contraseña incorrecta.") 
            else:
                print("///Este usuario no existe.")           
        else:
            print("///Opcion no valida, intente denuevo.")       
    else:
        option = str(initial)#opcion de cerrar el progrrma con la palabra pedida en la diapositiva
        if option == "SALIR":
            print("///saliendo...")
            break
        else:
            print("///Opcion desconocida, intente denuevo")    
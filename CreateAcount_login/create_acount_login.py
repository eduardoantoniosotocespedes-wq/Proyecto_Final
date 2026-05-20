print("////SISTEMA DE CONTROL DE VISITAS MEDICAS///")
employee  =["eduardo"]
password =[]
while True:
    print("-Eliga una una de las opciones.-")
    print("*1.-Crear cuenta.")
    print("*2.-Ingresar.")
    option = int(input("responda aqui: "))
    if option == 1:
        user =str(input("ingrese su nombre de usuario: "))
        if user  not in employee:
            employee.append(user)
        else:
            print("este usuario ya existe ingrese otro")    

        break
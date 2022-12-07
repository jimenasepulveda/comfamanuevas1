opcion=100

print("Empanadas el machetico")
print("*************************\n")

print("1. Registrar empanada")
print("2. Ver empanada")
print("0. Salir ")


empanadas=[]
while opcion != 0:
    opcion=int(input("Digita una opcion: "))
    if opcion==1:
        empanada=input("Digite el nombre de la empanada a registrar: ")
        empanadas.append(empanada)
    elif opcion==2:
        for empanada in empanadas:
            print(f'La empanada es: {empanada}')
    elif opcion==0:
        break
    else:
        print("Apreciado usuario, debes seleccionar una opcion valida...")
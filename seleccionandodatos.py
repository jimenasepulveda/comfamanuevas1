#Entradas del problema 
niveldeagua=int(input("digita el nivel de agua"))

#Eveluando caminos multiples (mas de 2)
if niveldeagua<=100:
    print("bajo nivel de agua")
elif niveldeagua >100 and niveldeagua<400:
    print("operacion optima")
elif niveldeagua >=400:
    print("peligro...")
else: 
    print("nivel de agua no valido")
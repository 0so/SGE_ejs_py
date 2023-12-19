#Pedir por pantalla nombre y apellidos y dar las 3 iniciales

nom = input("¿NOMBRE?: ")
ape = input("¿APELLIDOS?:")


def iniciales():
    init_nom = nom[0]
    apellidos = ape.split()  #Split a str into a list where each word is a list item
    print(apellidos)

    inits_apes = [ape[0] for ape in apellidos]
    init_ape = ''.join(inits_apes)
    print("Iniciales de los apellidos -> " , init_ape)
 
    return init_nom + init_ape


exit = iniciales()
print(f"Las tres iniciales son: {exit}")

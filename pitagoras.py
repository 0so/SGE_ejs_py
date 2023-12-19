import math
from colorama import Fore, Style, init
"""
v0.

cateto1 = int(input("Dime el cateto 1: "))
cateto2 = int(input("Dime el cateto 2:"))
hipotenusa = int(input("Dame la hipotenusa: "))

def pitagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

hipotenusa = pitagoras(cateto1, cateto2)
print(f"La longitud de la hipotenusa es: {hipotenusa}")

"""

#v1.
init(autoreset=True)

def hipotenusa(catetoA, catetoB):
    hipotenusa = math.sqrt(catetoA**2 + catetoB**2)
    return hipotenusa

def cateto(cateto, hipotenusa):
    cateto_unk = math.sqrt(hipotenusa**2 - cateto**2)
    return cateto_unk

def syso(mensaje, color=Fore.WHITE):
    print(color + mensaje + Style.RESET_ALL, end='')

syso("¿QUÉ QUIERES CALCULAR? (HIPOTENUSA/CATETO): ", Fore.BLUE)
op = input().lower()

if op == "hipotenusa":
    syso("Cateto a -> ", Fore.YELLOW)
    catetoA = float(input())
    syso("Cateto b -> ", Fore.YELLOW)
    catetoB = float(input())
    result = hipotenusa(catetoA, catetoB)
    syso(f"La hipotenusa mide {result}", Fore.GREEN)

elif op == "cateto":
    syso("¿Hipotenusa? -> ", Fore.YELLOW)
    h = float(input())
    syso("¿Cateto? -> ", Fore.YELLOW)
    c = float(input())
    try:
        result = cateto(c, h)
        syso(f"El cateto mide {result}", Fore.GREEN)
    except ValueError as e:
        syso(f"Error: {e}", Fore.RED)

else:
    syso("Opción no válida.", Fore.RED)
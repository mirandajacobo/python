from programas.suma import sumar2
from programas.restas import restar2
from vistas.menu import cargar_menu

from vistas.lineas import cargar_lineas
from datetime import datetime

import os

programa = True
os.system("clears")
print("Hora:", datetime.now().strftime("%H:%M:%Ss"))

while(programa):
    cargar_lineas(30)
    cargar_menu()
    res = int(input("|[?]"))
    if res == 1:
        print("sumar de numeros")
        sumar2()
    elif res == 2:
        print("restar dos numeros")
        restar2()
    elif res == 3:
        print("salir de programa")
        programa = False 

    os.system("clears")
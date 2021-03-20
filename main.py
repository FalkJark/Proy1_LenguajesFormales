import modules as md
import afds
import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename as ask

out = False

while out != True:
    md.menu()
    option = input("ingresa tu opción: ")

    if option == "1": # read file
        os.system("cls")
        print("Selecciona tu archivo: ")
        Tk().withdraw()
        filename = ask()

        archivo = open(filename)
        lines = archivo.readlines()
        archivo.close()
        
        row = 1
        for line in lines:
            afds.afd(line,row)
            line = line.rstrip("\n")
            row += 1
            
        for k in afds.tableTk:
            print(k.idTk,k.tk,k.lexemeTk,k.xTk,k.yTk)
        
        print("\n")
        aaaa = input("presione enter para continuar ")

    elif option == "6":
        print("Hasta pronto...")
        out = True
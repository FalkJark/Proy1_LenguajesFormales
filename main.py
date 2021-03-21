import modules as md
import afds
import syntax

import os
from tkinter import Tk
from tkinter.filedialog import askopenfilename as ask

out = False
#validations
menuV = False
pedidoV = False

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
        print("Leyendo linea por linea...")  
        for line in lines:
            afds.afd(line,row)
            line = line.rstrip("\n")
            row += 1
        
        row = 1
        print("Validando los tokens...")
        if len(afds.tableE) == 0:
            for line in lines:
                syntax.getValuesMenu(line,row)
                row+=1
            menuV = True
        else:
            print("Hay errores")
        #syntax.printRest() 
        #syntax.printSec()
        #syntax.printElement()

        #for k in afds.tableTk:
        #    print(k.idTk,k.tk,k.lexemeTk,k.xTk,k.yTk)
        
        print("\n")
        aaaa = input("presione enter para continuar ")

    elif option == "2":
        os.system("cls")
        print("Selecciona tu archivo: ")
        Tk().withdraw()
        filename = ask()

        archivo = open(filename)
        lines = archivo.readlines()
        archivo.close()
        
        row = 1  
        print("Leyendo linea por linea...") 
        for line in lines:
            afds.afd(line,row)
            line = line.rstrip("\n")
            row += 1
        
        row = 1
        print("Validando los tokens...")
        if len(afds.tableE) == 0:
            for line in lines:
                syntax.getValuesInvoice(line,row)
                row+=1
            pedidoV = True
        else:
            print("Hay errores")
        #for k in afds.tableTk:
         #   print(k.idTk,k.tk,k.lexemeTk,k.xTk,k.yTk)
        #syntax.printInvoices()
        #syntax.printDetails()
       
        
        print("\n")
        aaaa = input("presione enter para continuar ")

    elif option == "3":
        os.system("cls")
        if menuV == False:
            print("Aun no tienes cargado ningun menu")
        else:
            outPriceLimit = False
            while outPriceLimit != True:
                os.system("cls")
                print("¿Deseas colocar un limite a los precios?")
                op = input("si / no : ")
                if (op == "si"):
                    print("Puedes ingresar numeros flotantes, pero con un (.)")
                    max = input("Ingrese el monto máximo que desea gastar: ")
                    tempMenu = []
                    for j in syntax.elements:
                        if float(j.priceEle) <= float(max):
                            tempMenu.append(j)

                    for k in tempMenu:
                        print(k.nameEle)
                    outPriceLimit = True
                elif (op == "no"):
                    print()
                else:
                    print("solo se permite \'si\' o \'no\'")
                    aaaa = input("\npresione enter para continuar ")

        print("\n")
        aaaa = input("presione enter para continuar ")

    elif option == "4":
        os.system("cls")
        if pedidoV == False:
            print()
            
            #print("Aun no tienes cargado ningun pedido")
        else:
            print("Ya hay information")

        print("\n")
        aaaa = input("presione enter para continuar ")

    elif option == "6":
        print("Hasta pronto...")
        out = True
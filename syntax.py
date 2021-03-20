from afds import getLexeme
import db
restaurants = []
sections = []
elements = []

def getValuesMenu(line,posY):
    posX = 0
    char=line[posX]
    ac = ord(char)
    if ac == 114: #restaurant's name
        name = getLexeme(1,"Cadena",posY)
        res = db.restaurant(len(restaurants),name)
        restaurants.append(res)
    elif ac == 39:
        nameSec = getLexeme(1,"Cadena",posY)
        sec = db.section(0,len(sections),nameSec)
        sections.append(sec)
    elif ac == 91:
        iden = getLexeme(1,"Identificador",posY)
        nameE = getLexeme(1,"Cadena",posY)
        price = getLexeme(1,"Numero",posY)
        desc = getLexeme(2,"Cadena",posY)
        if len(sections)>0:
            element = db.element(iden,len(sections)-1,nameE,price,desc)
            elements.append(element)
        else:
            print("Hubo un error de sintaxis")

def printRest():
    if len(restaurants)>0:
        print("Restaurants")
        for i in restaurants:
            print("id: ",i.idRes,", name: ",i.nameRes)
    else:
        print("Array Restaurant is empty")

def printSec():
    if len(sections)>0:
        print("Sections")
        for i in sections:
            print("id_Res: ",i.idRes,", id_Sec: ",i.idSec,", name: ",i.nameSec)
    else:
        print("Array Sections is empty")

def printElement():
    if len(elements)>0:
        print("Elements")
        for i in elements:
            print("idSec: ",i.idSec,", id: ",i.idElement,", name: ",i.nameEle,", price: ",i.priceEle,", desc: ",i.descEle)
    else:
        print("Array Elements is empty")
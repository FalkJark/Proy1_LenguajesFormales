from afds import getLexeme
import db
restaurants = []
sections = []
elements = []

invoices = []
details = []

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
    print("Guardando información del menu...")

def getValuesInvoice(line,posY):
    posX = 0
    char=line[posX]
    ac = ord(char)
    if ac == 39:
        nameCli = getLexeme(1,"Cadena",posY)
        nitCli = getLexeme(2,"Cadena",posY)
        address = getLexeme(3,"Cadena",posY)
        tip = getLexeme(1,"Numero",posY)

        invoice = db.invoice(len(invoices),nameCli,nitCli,address,tip)
        invoices.append(invoice)

    elif ac >= 48 and ac<=57:
        cant = getLexeme(1,"Numero",posY)
        ident = getLexeme(1,"Identificador",posY)
        if len(invoices)>0:
            det = db.detail(len(details),len(invoices)-1,cant,ident)
            details.append(det)
        else:
            print("Hubo un error de sintaxis")
    print("Guardando información de la compra...")

def printInvoices():
    if len(invoices)>0:
        print("Invoices")
        for i in invoices:
            print("id: ",i.idInv,", name: ",i.nameCli,", nit: ",i.nitCli,", address: ",i.addressCli,", tip: ",i.tip)
    else:
        print("Array Invoices is empty")


def printDetails():
    if len(details)>0:
        print("Details")
        for i in details:
            print("id: ",i.idDet,"idInv: ",i.idInv,", cant: ",i.cant,", idProduct: ",i.idElement)
    else:
        print("Array Restaurant is empty")


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
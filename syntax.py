from afds import getLexeme

information = {}
#information['section'] = 

def getValuesMenu(line,posY):
    posX = 0
    char=line[posX]
    ac = ord(char)
    if ac == 114: #restaurant's name
        name = getLexeme(1,"Cadena",posY)
        information['name'] = name
    elif ac == 39:
        
        print("encontro una seccion")
    elif ac == 91:
        print("encontro una entrada")    
            #name = getLexeme(1,"Cadena",posY)
            #if name != None:
            #    information['name'] = name
#from afds import getLexeme

information = {}



def getValuesMenu(line,posY):
    posX = 0
    out = False
    while out != True:
        char=line[posX]
        ac = ord(char)
        #Nombre del restaurante
        if char == 114:
            name = getLexeme(1,"Cadena",posY)
            if name != None:
                information['name'] = name



#imports
from tokens import token
from errors import error

#global variables
reservada = "restaurante"
tableTk = []
tableE = [] 

# useful variables
idToken = 0
idError = 0

# test
l1 = "[d3;‘Desayuno 3’;35;’Descripción Desayuno 3’]"
l2 = "‘XX’, ‘xx’, ‘xx’, 8%"
l3 = "[ bebida_2;‘Bebida #2’;10.50; ’Descripción Bebida 2’]"
l4 = "[bebida_1;‘Bebida #1’;11.;’Descripción Bebida 1’ ]"
#-------------Automata finito determinista
def afd(line,posY):
    line = line + " "
    length = len(line)
    posX = 1
    state = 0
    cache = ''
    while posX <= length:
        char = line[posX-1]
        ac = ord(char)
        idToken = len(tableTk)
        idError = len(tableE)
        #--------------------SWITCH------------------------
        if state == 0:  
            if ac>=48 and ac<=57: # char is a number
                print("encontro un numero")
                cache += chr(ac)
                state = 5
                posX += 1
            else:
                posX += 1 # if dont exist

        elif state == 5: 
            if ac>=48 and ac<=57: # char is a number
                cache += chr(ac)
                state = 5
                posX += 1
            elif ac == 46: # char is a dot (.)
                cache += chr(ac)
                state = 6
                posX += 1
            elif ac == 37: # char is a symbol percent symbol (%)
                print("encontro un simbolo %")
                cache += chr(ac)
                state = 8
                posX += 1
            else:
                tk = token(idToken,"Entero",cache,posX,posY)
                tableTk.append(tk)
                state = 0
                cache = ''
        
        elif state == 6:
            if ac>=48 and ac<=57: # char is a number
                cache += chr(ac)
                state = 7
                posX += 1
            else:
                cache += "00"
                tk = token(idToken,"Flotante",cache,posX,posY)
                tableTk.append(tk)
                state = 0
                cache = ''
        
        elif state == 7:
            if ac>=48 and ac<=57: # char is a number
                cache += chr(ac)
                state = 7
                posX += 1
            else:
                tk = token(idToken,"Flotante",cache,posX,posY)
                tableTk.append(tk)
                state = 0
                cache = ''
        
        elif state == 8:
            tk = token(idToken,"Porcentaje",cache,posX,posY)
            tableTk.append(tk)
            state = 0
            cache = ''

        
        else:
            print("Algo salio mal, no hay ningun estado")
            break
            


afd(l4,0)


if len(tableTk) != 0:
    for i in tableTk:
        print("id: ",i.idTk,", valor: ",i.tk,", lexema: ",i.lexemeTk," posX: ",i.xTk)
else:
    print("token vacios")
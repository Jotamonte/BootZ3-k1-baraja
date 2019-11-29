
import random
_palos = ['o','c','e','b']
_cartas = ['A','2','3','4','5','6','7','S','C','R']

def baraja():
    result = []
    for palo in _palos:
        for carta in _cartas:
            result.append(carta + palo)
    
    return result

def elige_carta(i, longitud):
    return random.randint(0,longitud-1)   
'''
def elige_carta_fija(longitud):
    if i == longitud -1:
        return 0
    else:
        return i +1
'''
def mezclar(b):
    for i in range(len(b)):
        #Elegimos carta de intercambio al azar
        al_azar = elige_carta(i,len(b))

        #Cambiamos la carta por orden (i) por la carta elegida al azar
        aux = b[i]
        b[i] = b[al_azar]
        b[al_azar] = aux

    return b





'''
def mezclar(b):
    for i in range(len(b)):
        aux = b[i]
        if i == len(b)-1:
            b[i] = b[0]
            b[0] = aux
        else:
            b[i] = b[i+1]
            b[i+1] = aux
    return b
'''


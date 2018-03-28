#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants import *
from tm import TM

def f_pal(estado,lecturas):
    """
    Definicion de la funcion de transicion para palindromos
    Pensada para una maquina de 3 cintas
    Toma un estado y una 3-upla, con las lecturas actuales de la TM
    Devuelve un estado,una 3-upla con lo que debe escribirse y una 3-upla en {L,R,S}^3
    
    Nota: La tm da error si se intenta reescribir la cinta de solo lectura, con algo
    distinto a lo que ya tiene.
    """
    a,b,c = lecturas
    if estado == "Avanzador":
        # avanzar al final en la cinta de entrada
        if a != blankSym:
            return ("Avanzador",lecturas,(R,S,S))
        else:
            return ("Copiador",lecturas,(L,R,S))
    elif estado == "Copiador":
        # copiar la cinta
        if a != playSym:
            return ("Copiador",(a,a,c),(L,R,S))
        else:
            return ("Rebobinador",lecturas,(S,S,S))
    elif estado == "Rebobinador":
        # rebobinar
        if b != playSym:
            return ("Rebobinador",lecturas,(S,L,S))
        else:
            return ("Comparador",lecturas,(S,S,S))
    elif estado == "Comparador":
        # comparar
        if a == blankSym:
            return ("Impresor",(a,b,"1"),(S,S,S))
        elif a != b:
            return ("Impresor",(a,b,"0"),(S,S,S))
        else:
            return ("Comparador",lecturas,(R,R,S))
    else:
        return (estado,lecturas,(S,S,S))

palabra=input("Ingrese una palabra en {0,1}^*:")
t=TM(["Avanzador","Copiador","Rebobinador","Comparador","Impresor"],["0","1"],"Avanzador",["Impresor"],f_pal,[palabra])
t.correr()

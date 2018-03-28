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
    if estado == 0:
        # avanzar al final en la cinta de entrada
        if a != blankSym:
            return (0,lecturas,(R,S,S))
        else:
            return (1,lecturas,(L,R,S))
    elif estado == 1:
        # copiar la cinta
        if a != playSym:
            return (1,(a,a,c),(L,R,S))
        else:
            return (2,lecturas,(S,S,S))
    elif estado == 2:
        # rebobinar
        if b != playSym:
            return (2,lecturas,(S,L,S))
        else:
            return (3,lecturas,(S,S,S))
    elif estado == 3:
        # comparar
        if a == blankSym:
            return (4,(a,b,"1"),(S,S,S))
        elif a != b:
            return (4,(a,b,"0"),(S,S,S))
        else:
            return (3,lecturas,(R,R,S))
    else:
        return (estado,lecturas,(S,S,S))

palabra=input("Ingrese una palabra en {0,1}^*:")
t=TM([0,1,2,3,4],["0","1"],0,[4],f_pal,[palabra])
t.correr()

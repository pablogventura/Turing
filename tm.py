#!/usr/bin/env python
# -*- coding: utf-8 -*-

L = 0
R = 1
S = 2

playSym = "▷"
blankSym = "□"
epsilonSym = "ε"

def warning(s):
    print("WARNING: %s" % s)

def f_pal(estado,lecturas):
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
            return (3,lecturas,(S,R,S))
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
    

class Cinta(object):
    """
    Objeto para representar cintas infintas
    
    >>> c = Cinta("hola")
    >>> c
    (▷, hola)
    """
    def __init__(self,x=[],solo_lectura=False):
        self.u=[playSym]
        self.v=list(x)
        self.solo_lectura=solo_lectura
    def leer(self):
        return self.u[-1]
    def escribir(self,sym):
        if not self.solo_lectura:
            self.u[-1] = sym
        elif self.u[-1] != sym:
            assert False, "Intento de escritura en cinta de solo lectura"
    def left(self):
        if not len(self.u) <= 1:
            self.v.insert(0,self.u[-1])
            del self.u[-1]
        self._clean()
    def right(self):
        if self.v:
            self.u.append(self.v[0])
            del self.v[0]
        else:
            self.u.append(blankSym)
        self._clean()
    def _clean(self):
        while self.v and self.v[-1]==blankSym:
            del self.v[-1]
    def __repr__(self):
        if self.v:
            return "("+''.join(self.u) +", " + ''.join(self.v)+")"
        else:
            return "("+''.join(self.u) +", " + epsilonSym +")"

class TM(object):
    """
    Clase para las maquinas de turing
    """
    def __init__(self,estados,alfabeto,q_start,qs_finales,transicion,cintasro,cintasrw=2):
        self.estados = estados
        assert q_start in estados
        self.estado = q_start
        for q in qs_finales:
            assert q in estados
        self.qs_finales = qs_finales
        self.cintas=[Cinta(x,solo_lectura=True) for x in cintasro]
        self.cintas+=[Cinta(solo_lectura=False) for i in range(cintasrw)]
        self.delta = transicion
    def avanzar(self):
        estado, escrituras, movimientos = self.delta(self.estado,tuple(c.leer() for c in self.cintas))
        self.estado = estado
        for i,c in enumerate(self.cintas):
            c.escribir(escrituras[i])
            if movimientos[i] == L:
                c.left()
            elif movimientos[i] == R:
                c.right()
    def correr(self):
        while not self.paro():
            self.avanzar()
    def paro(self):
        return self.estado in self.qs_finales
    def __repr__(self):
        result = "TM(\n"
        for c in self.cintas:
            result += "\t%s,\n" % repr(c)
        result += ")"
        return result

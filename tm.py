#!/usr/bin/env python
# -*- coding: utf-8 -*-

playSym = "▷"
blankSym = "□"

def warning(s):
    print("WARNING: %s" % s)

class Cinta(object):
    """
    Objeto para representar cintas infintas
    
    >>> c = Cinta([e for e in "hola"])
    >>> c
    (▷, hola)
    """
    def __init__(self,x=[],solo_lectura=False):
        self.u=[playSym]
        self.v=x
        self.solo_lectura=solo_lectura
    def leer(self):
        return self.u[-1]
    def escribir(self,sym):
        if not self.solo_lectura:
            self.u[-1] = sym
        else:
            warning("Intento de escritura en una cinta de solo lectura")
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
            return "("+''.join(self.u) +", ε)"

class TM(object):
    """
    Clase para las maquinas de turing
    """
    def __init__(self):
        pass
    def avanzar(self):
        pass
    def correr(self):
        while not self.is_halted():
            self.avanzar()
    def paro(self):
        pass

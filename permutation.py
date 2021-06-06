from random import *
import numpy as np
import matplotlib.pyplot as plt
from math import *
import PlusProcheVoisinTest as ppt


def longueur (x,y,chemin):
    n=len(x)
    d=0
    for i in range(0,len(chemin)-1):
        d+=sqrt((x[chemin[i]]-x[chemin[i+1]])**2+(y[chemin[i]]-y[chemin[i+1]])**2)
    return d + sqrt((x[chemin[0]]-x[chemin[-1]])**2+(y[chemin[0]]-y[chemin[-1]])**2)



def permutation(x,y,ordre):
    d  = longueur(x,y,ordre)
    d0 = d+1
    it = 1
    while d < d0 :
        it += 1
        d0 = d
        for i in range(1,len(ordre)-1) :
            for j in range(i+2,len(ordre)+1):
                r = ordre[i:j].copy()
                r.reverse()
                ordre2 = ordre[:i] + r + ordre[j:]
                t = longueur(x,y,ordre2)
                if t < d :
                    d = t
                    ordre = ordre2
    return ordre

def n_permutation(x,y,ordre, miniter):
    bordre = ordre.copy()
    d0 = longueur(x,y,ordre)
    for i in range(0,20):
        print("iteration",i, "d=",d0)
        shuffle(ordre[1:])
        ordre = permutation (x,y,ordre)
        d = longueur(x,y,ordre)
        if d < d0 :
            d0 = d
            bordre = ordre.copy()
    return bordre
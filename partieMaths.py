from random import *
import numpy as np
import matplotlib.pyplot as plt
from math import *
import PlusProcheVoisinTest as ppt
import permutation as perm


class Algo ():

    def __init__(self,x,y,n,xmax,ymax,xinit,yinit):
        self.n=n
        self.xmax=xmax
        self.ymax=ymax
        self.x=x
        self.y=y
        self.liste=list([[self.x[i],self.y[i]] for i in range(len(self.x))])
        self.xinit=xinit
        self.yinit=yinit


    def longueur (self,chemin):
        d=0
        for i in range(0,len(chemin)-1):
            d+=sqrt((self.x[chemin[i]]-self.x[chemin[i+1]])**2+(self.y[chemin[i]]-self.y[chemin[i+1]])**2)
        return d + sqrt((self.x[chemin[0]]-self.x[chemin[-1]])**2+(self.y[chemin[0]]-self.y[chemin[-1]])**2)


    def permutation(self,ordre):
        d  = self.longueur(ordre)
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
                    t = self.longueur(ordre2)
                    if t < d :
                        d = t
                        ordre = ordre2
        return ordre

    def listeChemins(self):
        M=[]
        N=[]
        D=[]
        for i in range(len(self.liste)):
            L=list(self.liste)
            p=ppt.PlusProcheVoisin(L,i,n-1,xmax,ymax)
            M.append([len(self.liste)]+p.listePlusProche())

        self.x.append(self.xinit)
        self.y.append(self.yinit)
        self.liste=list([[self.x[i],self.y[i]] for i in range(len(self.x))])

        for j in range(0, len(self.liste)-1):
            N.append(self.permutation(M[j]))
            D.append(self.longueur(self.permutation(M[j])))

        a=min(D)
        b=D.index(a)

        return(N[b])


    def pointsNouvelOrdre(self,chemin,x,y):
        L=[[self.xinit,self.yinit]]
        for i in range(1,len(x)):
            a=chemin.index(i)
            L.append([x[a],y[a]])
        return L



#
# n=15
# xmax=10
# ymax=10
# xinit=0
# yinit=0
#
#
# #liste des coordonnées sans le point de départ
# x = [ np.random.uniform(0,xmax) for _ in range(n) ]
# y = [ np.random.uniform(0,ymax) for _ in range(n) ]
#
#
# A=Algo(x,y,n,xmax,ymax,xinit,yinit)
# chemin=A.listeChemins()
# nouveauxPoitns=A.pointsNouvelOrdre(chemin,x,y)


from random import *
import numpy as np
import matplotlib.pyplot as plt
from math import *




def creerPoints(n,xmax,ymax):
    Liste=[]
    while len(Liste)!=n:
        L=[]
        L.append(np.random.uniform(0,xmax))
        L.append(np.random.uniform(0,ymax))
        if L not in Liste:
            Liste.append(L)
    return Liste



##


def distance(point1,point2):
    x1,y1=point1[0],point1[1]
    x2,y2=point2[0],point2[1]
    return sqrt((x1-x2)**2+(y1-y2)**2)

class PlusProcheVoisin():

    def __init__(self,T,ref,n,xmax,ymax):#ref<n
        self.n = n
        self.xmax = xmax
        self.ymax = ymax
        self.Liste = list(T)
        self.L1 = []
        self.L2 = []
        self.T=T
        self.ref=ref


    def distance(self,point1,point2):
        x1,y1=point1[0],point1[1]
        x2,y2=point2[0],point2[1]
        return sqrt((x1-x2)**2+(y1-y2)**2)


    def pointPlusProche(self):

        D=[] #liste des distance au point ref
        for i in range (len(self.Liste)):
                D.append(self.distance(self.Liste[self.ref],self.Liste[i]))
        #print(D)
        D[self.ref]=sqrt(self.xmax**2+self.ymax**2)
        return(D.index(min(D)))

    def listePlusProche(self):

        m=0
        for i in range (len(self.Liste)):
            self.L1.append(self.ref)
            m=self.pointPlusProche()
            self.Liste[self.ref]=[10000,10000]
            self.ref=m




    def nouvelleCoord(self):
        self.listePlusProche()
        #on remet les points dans le bon ordre et on rajoute le dernier

        for i in range(len(self.T)):
            self.L2.append(self.T[self.L1[i]])
        return self.L2

    @classmethod
    def trace(cls,p):
        p.nouvelleCoord()

        #on separe les point en x,y
        X=[]
        Y=[]
        for j in range(len(p.L2)):
            X.append(p.L2[j][0])
            Y.append(p.L2[j][1])

        #on trace
        x = np.array(X)
        y = np.array(Y)
        plt.plot(x, y,'r+-')

        plt.show()


    @classmethod
    def distanceParcourt(cls,Liste):

        a=0

        for i in range(len(Liste)-1):
            a+=distance(Liste[i],Liste[i+1])

        return  a


def listeChemins():
    M=[]

    for i in range(len(Liste)):
        L=list(Liste)
        p=PlusProcheVoisin(L,i,n,xmax,ymax)
        M.append([len(Liste)]+p.listePlusProche())


        return(M)

n=15
xmax=5
ymax=5

Liste=creerPoints(n,xmax,ymax)

p=PlusProcheVoisin(Liste,0,n,xmax,ymax)

# # print(p.Liste)
# # print('')
# # print(p.pointPlusProche())
# print(p.listePlusProche())
# print('')
# print(Liste)
# PlusProcheVoisin.trace(p)
#
#
# # print(listeChemins())
# # print('')
# # print(distanceParcourt(listeChemins()[0],Liste))
# # print('')
#
# ##
# # Liste.append([xinit,yinit])
# # print(Liste)
# # print("")

ltest=[[1,1],[1,3],[1,4],[1,2]]
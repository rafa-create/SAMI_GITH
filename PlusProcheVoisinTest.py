from random import *
import numpy as np
import matplotlib.pyplot as plt
from math import *

##

class PlusProcheVoisin():

    def __init__(self,T,ref,n,xmax,ymax):#ref<n
        self.n = n
        self.xmax = xmax
        self.ymax = ymax
        self.Liste = list(T)
        self.L1 = []
        self.L2 = []
        self.T=list(T)
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

        return(self.L1)




    def nouvelleCoord(self):
        #on remet les points dans le bon ordre et on rajoute le dernier

        for i in range(len(self.T)):
            self.L2.append(self.T[self.L1[i]])
        #self.L2.append(self.L2[0])


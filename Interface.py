from tkinter import *
from random import randrange
from random import randrange
from time import sleep



class Application():
    def __init__(self,Points_a_atteindre,position_lego):
        self.Points_a_atteindre=Points_a_atteindre
        self.position_lego=position_lego
    #Création de la fenêtre principale (main window)
        self.Mafenetre=Tk()
        self.Mafenetre.title('Suivi du robot en direct')
    # zone de dessin
        self.can=Canvas(self.Mafenetre,width=1180,height=600,bg='cyan')
        self.can.pack(side=TOP,padx=5,pady=5)
    #informer l'utilisateur sur la couleur du Lego
        self.lego = self.can.create_rectangle(100,100,110,110,fill='dark green')
        self.lu,self.lv,self.chemin = [100,112],[100,112],[]
        self.chemin.append(self.lego)
    #commande au clavier
        self.can.bind_all('<Up>', self.haut)
        self.can.bind_all('<Down>', self.bas)
        self.can.bind_all('<Left>', self.gauche)
        self.can.bind_all('<Right>', self.droite)
        self.can.bind_all('p',self.pause)
        self.can.create_rectangle(10,405,130,425,fill="lightblue")
        self.can.create_text(60,415,text='Position du Lego',fill="black")
        r=7
        self.can.create_oval(120-r,415-r,120+r,415+r,fill="red")
    #informer l'utilisateur sur la couleur des Points_a_atteindre
        d=30
        self.can.create_rectangle(10,405-d,130,425-d,fill="lightblue")
        self.can.create_text(60,415-d,text='Points à atteindre',fill="black")
        self.can.create_oval(120-r,415-d-r,120+r,415+r-d,fill="yellow")
        for i in range(7):
            pX = randrange(5, 1180)
            pY = randrange(5, 600)
            self.can.create_oval(pX-r, pY-r, pX+r, pY+r,fill="yellow")
    def deplacement(self):
        global a,b,z,y,j,m
        c=len(self.chemin)
        sleep(0.3)
        #Chaque carré reprend la coordonnée du précédent dans la liste (chemin)
        while c!=0 :
                self.lu[c]=self.lu[c-1]
                self.lv[c]=self.lv[c-1]
                c+=-1
        self.can.create_rectangle(self.lu[c]+3,self.lv[c]+3,self.lu[c]+7,self.lv[c]+7,fill='black')
        self.can.coords(self.chemin[c],self.lu[c],self.lv[c],self.lu[c]+10,self.lv[c]+10)
        #On change les coordonées du premier carré
        self.lu[0] += a
        self.lv[0] += b
        #On applique les nouvelles coordonnées aux carrés correspondant
        self.can.coords(self.chemin[c],self.lu[c],self.lv[c],self.lu[c]+10,self.lv[c]+10)
        c=1
        #Si le chemin est mord un coté il ressort de l'autre
        #autre coté du canvevas:
        d=1
        if self.lu[0]==200:
                self.lu[0],d=10,0
        if self.lu[0]==0 and d==1:
                self.lu[0]=200
        if self.lv[0]==200:
                self.lv[0],d=10,0
        if self.lv[0]==0 and d==1:
                self.lv[0]=200
        d=0
        #Si le lego de tête recoupe le cercle
        if j!=1 and m!=1:
                self.Mafenetre.after(100,self.deplacement)
    def gauche(self,event):
        global a,b,s
        a=-10
        b=0
        if s==0:
                s=1
                self.deplacement()
    def droite(self,event):
        global a,b,s
        a=10
        b=0
        if s==0:
                s=1
                self.deplacement()
    def haut(self,event):
        global a,b,s
        a=0
        b=-10
        if s==0:
                s=1
                self.deplacement()
    def bas(self,event):
        global a,b,s
        a=0
        b=10
        if s==0:
                s=1
                self.deplacement()
    def pause(self,event):
        global j,a,b,m
        t=0
        if a==b:
                t=1
        if j!=1:
                #Affichage ou Effacage du texte 'PAUSE'
                #Et arrêt
                if m!=1:
                        m=1
                else:
                        m=0
                        if t!=1:
                                self.deplacement()

s=j=m=t=a=b=0
z=y=50


App=Application(6,7)
App.Mafenetre.mainloop()
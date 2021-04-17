from tkinter import *
from random import randrange
from random import randrange
from time import sleep


class Interface():
    def __init__(self,Points_a_atteindre,position_lego):
        self.Points_a_atteindre=Points_a_atteindre
        self.position_lego=position_lego
        self.cote=600
    #initialisation des variables
        self.s=self.j=self.m=self.t=self.a=self.b=0
    #Création de la fenêtre  
        self.Mafenetre=Tk()
        self.Mafenetre.title('Suivi du robot en direct')
    # zone de dessin
        self.can=Canvas(self.Mafenetre,width=self.cote,height=self.cote,bg='cyan')
        self.can.pack(side=TOP,padx=5,pady=5)
    #informer l'utilisateur de la couleur du Lego
        rl=5
        self.lego = self.can.create_oval(120-rl,415-rl,120+rl,415+rl,fill="red")
        self.lu,self.lv,self.chemin = [100,112],[100,112],[]
        self.chemin.append(self.lego)
    #commande au clavier
        self.can.bind_all('<Up>', self.haut)
        self.can.bind_all('<Down>', self.bas)
        self.can.bind_all('<Left>', self.gauche)
        self.can.bind_all('<Right>', self.droite)
        self.can.bind_all('p',self.pause)
     #informer l'utilisateur sur la couleur du lego
        self.can.create_rectangle(10,405,130,425,fill="lightblue")
        self.can.create_text(60,415,text='Position du Lego',fill="black")
        self.can.create_oval(120-rl,415-rl,120+rl,415+rl,fill="red")
    #informer l'utilisateur sur la couleur des Points_a_atteindre
        r=7
        d=50
        self.can.create_rectangle(10,405-d,130,425-d,fill="lightblue")
        self.can.create_text(60,415-d,text='Points à atteindre',fill="black")
        self.can.create_oval(120-r,415-d-r,120+r,415+r-d,fill="yellow")
        for i in range(7):
            pX = randrange(5, self.cote)
            pY = randrange(5, self.cote)
            self.can.create_oval(pX-r, pY-r, pX+r, pY+r,fill="yellow")
    def deplacement(self):
        c=len(self.chemin)
    #Chaque carré reprend la coordonnée du précédent dans la liste (chemin)
        while c!=0 :
                self.lu[c]=self.lu[c-1]
                self.lv[c]=self.lv[c-1]
                c+=-1
    #On fait la trace
        self.can.create_rectangle(self.lu[c]+3,self.lv[c]+3,self.lu[c]+7,self.lv[c]+7,fill='black')
    #On change les coordonées du Lego
        self.lu[0] += self.a
        self.lv[0] += self.b
    #On applique les nouvelles coordonnées aux carrés correspondant
        self.can.coords(self.chemin[c],self.lu[c],self.lv[c],self.lu[c]+10,self.lv[c]+10)
    #commande pour la pause
        if self.j!=1 and self.m!=1:
            self.can.after(100,self.deplacement)
    def gauche(self,event):
        self.a=-10
        self.b=0
        if self.s==0:
                self.s=1
                self.deplacement()
    def droite(self,event):
        self.a=10
        self.b=0
        if self.s==0:
                self.s=1
                self.deplacement()
    def haut(self,event):
        self.a=0
        self.b=-10
        if self.s==0:
                self.s=1
                self.deplacement()
    def bas(self,event):
        self.a=0
        self.b=10
        if self.s==0:
                self.s=1
                self.deplacement()
    def pause(self,event):
        self.t=0
        if self.a==self.b:
                self.t=1
        if self.j!=1:
                if self.m!=1:
                        self.m=1
                else:
                        self.m=0
                        if self.t!=1:
                                self.deplacement()

Interface(8,5).Mafenetre.mainloop()

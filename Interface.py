from random import randrange
from tkinter import *

class Interface():
    def __init__(self,Points_a_atteindre):
    #initialisation des variables graphiques
        self.pres=5
        self.trace=0.5
        self.tlego=14
        self.Points_a_atteindre=Points_a_atteindre
        self.cote=600
        self.s=self.j=self.m=self.t=self.a=self.b=0
    #Création de la fenêtre
        self.Mafenetre=Tk()
        self.Mafenetre.title('Suivi du robot en direct')
    # zone de dessin
        self.can=Canvas(self.Mafenetre,width=self.cote,height=self.cote,bg='cyan')
        self.can.pack(side=TOP,padx=5,pady=5)
    #informer l'utilisateur sur la couleur du lego
        b=167#décalage vers le bas des panneaux
        rl=7
        self.can.create_rectangle(10,405+b,130,425+b,fill="lightblue")
        self.can.create_text(60,415+b,text='Position du Lego',fill="black")
        self.can.create_oval(120-rl,415-rl+b,120+rl,415+rl+b,fill="red")
    #informer l'utilisateur sur la couleur des Points_a_atteindre
        r=7
        d=30#decalage entre les deux panneaux
        self.can.create_rectangle(10,405-d+b,130,425-d+b,fill="lightblue")
        self.can.create_text(60,415-d+b,text='Points à atteindre',fill="black")
        self.can.create_oval(120-r,415-d-r+b,120+r,415+r-d+b,fill="yellow")
    #initialisation lego
        self.lego =self.can.create_oval(120-rl,415-rl+b,120+rl,415+rl+b,fill="red")
        self.lu,self.lv,self.chemin = [1000,1000],[10000,1000],[]#hors du cadre
        self.chemin.append(self.lego)
    #Tracé des points à atteindre
        for i in range(7):
            [pX,pY]= self.Points_a_atteindre[i]
            self.can.create_oval(pX-r, pY-r, pX+r, pY+r,fill="yellow")
    #lancer l'affichage du robot
        self.deplacement()
    def deplacement(self):
        c=len(self.chemin)
    #Chaque carré reprend la coordonnée du précédent dans la liste (chemin)
        while c!=0 :
                self.lu[c]=self.lu[c-1]
                self.lv[c]=self.lv[c-1]
                c+=-1
    #On fait la trace
        self.can.create_rectangle(self.lu[c]+self.trace+7,self.lv[c]+self.trace+7,self.lu[c]-self.trace+7,self.lv[c]-self.trace+7,fill='black')
    #coordonnées du lego ici
        self.lu[0] =100 #INSERER ABSCISSE ROBOT
        self.lv[0] =100#INSERER ordonnée ROBOT
    #On applique les nouvelles coordonnées aux carrés correspondant
        self.can.coords(self.chemin[c],self.lu[c],self.lv[c],self.lu[c]+self.tlego,self.lv[c]+self.tlego)
    #On peut modifier la vitesse d'actualisation ici
        self.can.after(300,self.deplacement)

Points_a_atteindre=[[466,362],[45,444],[54,380],[438,44],[559,129],[243,234],[342,331]]
Interface(Points_a_atteindre).Mafenetre.mainloop()
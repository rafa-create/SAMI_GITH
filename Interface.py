
from tkinter import *


class Application():
    def __init__(self,Points_a_atteindre,nbr_colonnes):
        self.jeu=Jeu()
        self.c=1
        self.tour=0
        self.joueur=1
        self.Points_a_atteindre=Points_a_atteindre
        self.nbr_colonnes=nbr_colonnes
        self.color = ["red", "#EDEF3A"]
    #Création de la fenêtre principale (main window)
        self.Mafenetre=Tk()
        self.Mafenetre.title('Suivi du robot en direct')
    #Création des bouton
        self.Quitter=Button(self.Mafenetre, text="Quitter", command=self.Mafenetre.destroy)
        self.Nj=Button(self.Mafenetre, text="Nouveau Jeu", command=self.nouveu_jeu)
    #Placement automatique du bouton
        self.Nj.pack()
        self.Quitter.pack()
    # zone de dessin
        self.can=Canvas(self.Mafenetre,width=400,height=430,bg='blue')
        self.can.pack(side=TOP,padx=5,pady=5)
        self.d=self.can.create_text(200,350,text='',fill=self.color[self.joueur-1])
    #rectangle avec les info du robot
        self.can.create_rectangle(18,405,92,425,fill="lightblue")
        self.can.create_text(47,415,text='Robot',fill="blue")
        r=7
        self.can.create_oval(77-r,415-r,77+r,415+r,fill="red")
    #rectangle avec les info des Points_a_atteindre
        self.can.create_rectangle(18,405,92,425,fill="lightblue")
        self.can.create_text(47,415,text='Robot',fill="blue")
        r=7
        self.can.create_oval(77-r,415-r,77+r,415+r,fill="red")
    def nouveu_jeu(self):
        self.dessiner_plateau()
        self.tour=0
        self.jeu.plateau=[]
        self.c=1
        self.can.itemconfig(self.d,text='')
        for i in range (6):
            self.jeu.plateau.append([0,0,0,0,0,0,0])
        self.can.bind('<Button-1>', self.click)



App=Application(6,7)
App.Mafenetre.mainloop()

from tkinter import *
from random import randrange


class Application():
    def __init__(self,Points_a_atteindre,nbr_colonnes):
        self.Points_a_atteindre=Points_a_atteindre
        self.nbr_colonnes=nbr_colonnes
        self.color = ["red", "#EDEF3A"]
    #Création de la fenêtre principale (main window)
        self.Mafenetre=Tk()
        self.Mafenetre.title('Suivi du robot en direct')
    #Création des bouton
        #self.Quitter=Button(self.Mafenetre, text="Quitter", command=self.Mafenetre.destroy)
    #Placement automatique du bouton
        #self.Quitter.pack()
    # zone de dessin
        self.can=Canvas(self.Mafenetre,width=1180,height=600,bg='cyan')
        self.can.pack(side=TOP,padx=5,pady=5)
    #rectangle avec les info du robot
        self.can.create_rectangle(18,405,92,425,fill="lightblue")
        self.can.create_text(47,415,text='Position du Lego',fill="black")
        r=7
        self.can.create_oval(77-r,415-r,77+r,415+r,fill="red")
    #rectangle avec les info des Points_a_atteindre
        d=100
        self.can.create_rectangle(18+d,405,d+92,425,fill="lightblue")
        self.can.create_text(47+d,415,text='Points à atteindre',fill="black")
        self.can.create_oval(77-r+d,415-r,77+d+r,415+r,fill="yellow")
        for i in range(7):
            pX = randrange(5, 1180)
            pY = randrange(5, 600)
            self.can.create_oval(pX-r, pY-r, pX+r, pY+r,fill="yellow")
            #On joute un nouveau point au serpent


App=Application(6,7)
App.Mafenetre.mainloop()

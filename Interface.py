from tkinter import *
from random import randrange


class Application():
    def __init__(self,Points_a_atteindre,poistion_lego):
        self.Points_a_atteindre=Points_a_atteindre
        self.poistion_lego=poistion_lego
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
    #informer l'utilisateur sur la couleur du Lego
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
            #On joute un nouveau point au serpent


App=Application(6,7)
App.Mafenetre.mainloop()

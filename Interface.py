#OUELAZOE
class Jeu():
    def __init__(self):
        plateau=[]
        for i in range (6):
            plateau.append([0,0,0,0,0,0,0])
        self.plateau=plateau
        self.joueurs=['Rafael','Noé']#Ici pour modifier les noms des joueurs !
        self.num_colonne=len(self.plateau[0])
        self.nbr_ligne=len(self.plateau)
    def afficher(self):
        for i in reversed(range(len(self.plateau))):
            for j in range(len(self.plateau[i])):
                if self.plateau[i][j]==0:
                    print('|',' ',end=' ')
                elif self.plateau[i][j]==1:
                    print('|','X',end=' ')
                elif self.plateau[i][j]==2:
                    print('|','O', end=' ')
            print('|')
        print('------------------------------')
        print('  1   2   3   4   5   6   7   ')
        print(self.plateau)

    def combiendanscolonne(self,num_colonne):
        compteur=0

        for i in range(len(self.plateau)):
            if self.plateau[i][num_colonne] !=0:
                compteur+=1
        return compteur

    def combien_dans_la_direction(self,i,j,delta_i,delta_j):
        compteur=0
        couleurpion=self.plateau[i][j]
        while (i+delta_i>=0 and i+delta_i<len(self.plateau)) and (j+delta_j>=0 and j+delta_j<len(self.plateau[0])) and self.plateau[i+delta_i][j+delta_j]==couleurpion:
            compteur+=1
            i=i+delta_i
            j=j+delta_j
        return compteur

    def empiler(self,couleurpion,num_colonne) :
        nbrpionscolonne=self.combiendanscolonne(num_colonne)#on pars du haut car c'est ainsi dans le tableau de chiffre mais on laisse le +1(2 pions..3 eme ligne donc2eme en python)
        if nbrpionscolonne == 6:
            return("Cette colonne est remplie")
        self.plateau[nbrpionscolonne][num_colonne]=couleurpion#on rajoute le pion au plateau

    def test_lignes(self,num_colonne):
        if self.combiendanscolonne(num_colonne)==0:
            return False
        i=self.combiendanscolonne(num_colonne)-1#on pars du haut car c'est ainsi dans le tableau de chiffre
        j=num_colonne
        return self.combien_dans_la_direction(i,j,0,1)+self.combien_dans_la_direction(i,j,0,-1) >=3

    def test_colonnes(self,num_colonne):
        if self.combiendanscolonne(num_colonne)==0:
            return False
        i=self.combiendanscolonne(num_colonne)-1#on pars du haut car c'est ainsi dans le tableau de chiffre
        j=num_colonne
        return self.combien_dans_la_direction(i,j,1,0)+self.combien_dans_la_direction(i,j,-1,0) >=3

    def test_diagonales(self,num_colonne):
        if self.combiendanscolonne(num_colonne)==0:
            return False
        i=self.combiendanscolonne(num_colonne)-1#on pars du haut car c'est ainsi dans le tableau de chiffre
        j=num_colonne
        #print(self.combien_dans_la_direction(i,j,1,1)+self.combien_dans_la_direction(i,j,-1,-1))
        #print(self.combien_dans_la_direction(i,j,-1,1)+self.combien_dans_la_direction(i,j,1,-1))
        return self.combien_dans_la_direction(i,j,1,1)+self.combien_dans_la_direction(i,j,-1,-1) >=3 or self.combien_dans_la_direction(i,j,-1,1)+self.combien_dans_la_direction(i,j,1,-1)>=3

    def test_tout(self,num_colonne):
            return self.test_lignes(num_colonne) or self.test_colonnes(num_colonne) or self.test_diagonales(num_colonne)

from tkinter import *


class Application():
    def __init__(self,nbr_lignes,nbr_colonnes):
        self.jeu=Jeu()
        self.c=1
        self.tour=0
        self.joueur=1
        self.nbr_lignes=nbr_lignes
        self.nbr_colonnes=nbr_colonnes
        self.color = ["red", "#EDEF3A"]
    #Création de la fenêtre principale (main window)
        self.Mafenetre=Tk()
        self.Mafenetre.title('Le Jeu du Puissance 4')
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
    #rectangle avec les info do joueur
        self.can.create_rectangle(18,405,92,425,fill="lightblue")
        self.can.create_text(47,415,text='Joueur',fill="blue")
        r=7
        self.can.create_oval(77-r,415-r,77+r,415+r,fill="red")
    #fonction pour créer les cercles blancs
    def dessiner_plateau(self):
        for i in range(7):
            for j in range(6):
                self.can.create_oval(20+i*52,15+j*52,70+i*52,j*52 + 65,fill="white")
    def nouveu_jeu(self):
        self.dessiner_plateau()
        self.tour=0
        self.jeu.plateau=[]
        self.c=1
        self.can.itemconfig(self.d,text='')
        for i in range (6):
            self.jeu.plateau.append([0,0,0,0,0,0,0])
        self.can.bind('<Button-1>', self.click)
    def click(self,event): #En cas de click
            x=event.x
            r=7
            if self.c==1:
                for i in range (7):
                    if 20+i*52 <x <70+i*52:
                        self.num_colonne=i
                        self.jeu.combiendanscolonne(self.num_colonne)
                        if not self.jeu.combiendanscolonne(self.num_colonne)== 6:
                            self.tour+=1
                            self.joueur=self.tour%2
                            self.jeu.empiler(self.joueur+1,self.num_colonne)
                            self.j=6-self.jeu.combiendanscolonne(self.num_colonne)
                            self.can.create_oval(77-r,415-r,77+r,415+r,fill=self.color[self.joueur])
                            self.can.create_oval(20+i*52,15+self.j*52,70+i*52,self.j*52 + 65,fill=self.color[self.joueur-1])
                            #self.jeu.afficher()
                            if self.jeu.test_tout(self.num_colonne):
                                self.c=0
                                self.can.itemconfig(self.d,text='Vous avez gagnez !',fill=self.color[self.joueur-1])


#Lancement du gestionaire d'événement
App=Application(6,7)
App.Mafenetre.mainloop()

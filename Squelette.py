from PlusProcheVoisin import *
from Interface import Application
from  ev3dev2.motor  import  OUTPUT_A , OUTPUT_B , LargeMotor
import sys, os
import mocap_node as mcn

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'src'))

###

class RoboLego():
    def __init__(self,name="Lego1",nomDeConfig="Mon Nom De Config",cst=None):

        #Le nom du robot(pour utiliser les commandes)
        self.__name=name

        #Le Motion Capture node du robot
        self.__mcn=mcn.MocapNode(nomDeConfig)

        #On récupère sa position initiale
        self.__mcn.run()
        self.__mcn.UpdateModelInfo()
        self.__position, self.__yaw = self.__mcn.getPos2DAndYaw(self.__name)
        self.__mcn.stop()

        #Eventuelles constantes pour paramétrer le robot
        self.__constantes=cst

        #La future interface du robot
        self.__interface=None

        #Le moteur gauche et droit du robot, à modifier en fonction du robot utilisé
        self.__lmotor , self.__rmotor = [LargeMotor(address) for  address  in (OUTPUT_A , OUTPUT_B)]


    def recupererNoeuds(self,nom_fichier="fichier_de_points"):
        """Prends en parametre le du fichier texte contenant les noeuds. Renvoie un liste de noeuds."""
        fichier=open(nom_fichier)
        txt=fichier.read()
        points=txt.split("\n")
        listeNoeuds=[]
        for p in points:
            coordonnee=p.split("\t")
            coordonnee[0],coordonnee[1]=float(coordonnee[0]),float(coordonnee[1])
            listeNoeuds.append(coordonnee)

        return listeNoeuds


    def ordreNoeuds(self,listeNoeuds):
        """Prend en parametre une liste de noeuds. Renvoie la liste des noeuds dans le bon ordre de passage. """
        k=PlusProcheVoisin(listeNoeuds,0,len(listeNoeuds),1000,1000)
        k.listePlusProche()
        self.listeNoeuds=k.nouvelleCoord()


    def partieAuto(self):
        """A compléter."""
        pass

    def cestParti(self,nom_fichier="fichier_de_points"):
        """Lance le robot. Prend en parametre une le nom du fichier contennt les noeuds. Utilise ordreNoeuds() pour ordonner les points, avant de lancer l'interface graphique et la partieAuto pour permettre au robot d'effectuer le trajet."""
        listeNoeuds=self.ordreNoeuds(self.recupererNoeuds(nom_fichier))
        self.__interface=Application(listeNoeuds,self.__position)
        self.__mcn.run()
        # self.__interface.Mafenetre.mainloop()
        # self.partieAuto()
        self.__mcn.stop()

###

rob=RoboLego()

rob.cestParti(r'C:\Users\Remis\Documents\GitHub\SAMI\fichier_de_points.txt')

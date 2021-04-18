from PlusProcheVoisin import *
from Interface import *
from  ev3dev2.motor  import  OUTPUT_A , OUTPUT_B , LargeMotor
import sys, os
import mocap_node as mcn

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'src'))

###

class RoboLego():
    def __init__(self,name="Lego1",nomDeConfig="Mon Nom De Config",cst=None):
        self.__name=name

        self.__mcn=mcn.MocapNode(nomDeConfig)

        self.__mcn.run()

        self.__mcn.UpdateModelInfo()
        self.__position, self.__yaw = self.__mcn.getPos2DAndYaw(self.__name)

        self.__mcn.stop()

        self.__listeNoeuds=[]
        self.__constantes=cst
        self.__interface=None
        self.__lmotor , self.__rmotor = [LargeMotor(address) for  address  in (OUTPUT_A , OUTPUT_B)]



    def recupererNoeuds(self,nom_fichier="fichier_de_points"):
        """Prends en parametre l'adresse du fichier texte contenant les noeuds. Renvoie un liste de noeuds."""
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
        """Prend en parametre une liste de noeuds. Actionne les roues du robot pour le faire se déplacer depuis sa position actuelle vers chaque noeud dans l'ordre de la liste."""



    def cestParti(self,nom_fichier):
        """Lance le robot. Prend en parametre une adresse Utilise ordreNoeuds() et allerVers() pour emmener le robot à destination."""
        listeNoeuds=self.ordreNoeuds(self.recupererNoeuds(nom_fichier))
        self.__interface=Application(self.__listeNoeuds,self.__position)
        self.__mcn.run()
        # self.__interface.Mafenetre.mainloop()
        # self.partieAuto()
        self.__mcn.stop()

###

rob=RoboLego()

rob.cestParti(r'C:\Users\Remis\Documents\GitHub\SAMI\fichier_de_points.txt')

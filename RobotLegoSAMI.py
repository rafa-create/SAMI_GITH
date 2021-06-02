from PlusProcheVoisin import *
# from  ev3dev2.motor  import  OUTPUT_C , OUTPUT_B , LargeMotor
import sys, os

sys.path.append(os.path.join(os.path.dirname(sys.path[0]),'Optitrack\\src'))

import mocap_node as mcn

from pannel import *
from time import *

###

class RobotLego():
    def __init__(self,adresseIP="100.75.155.131",name="Lego1",nomDeConfig="PC4"):

        #Le nom du robot(pour utiliser les commandes)
        self.name=name
        self.client=TCPClient()
        self.adresseIP=adresseIP

        #Le Motion Capture node du robot
        self.mcn=mcn.MocapNode(nomDeConfig)

        #On récupère sa position initiale
        self.mcn.run()
        self.mcn.updateModelInfo()
        self.position, self.yaw = self.mcn.getPos2DAndYaw(self.name)
        self.mcn.stop()

        #La future interface du robot
        self.interface=None

        # #Le moteur gauche et droit du robot, à modifier en fonction du robot utilisé
        # self.lmotor , self.rmotor = [LargeMotor(address) for  address  in (OUTPUT_C , OUTPUT_B)]


    def recupererNoeuds(self,nom_fichier="fichier_de_points.txt"):
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
        return listeNoeuds


    def commandeRobot(self,Position):     # Position: liste des positions à récupérer de la partie maths
        """Foncion qui permet au robot de faire tout le parcours en fonction d'"""
        erreur=3
        k1=30
        k2=1
        k3=1
        vmax=50
        delta=12.8
        Ks=0.5

        self.client.connect(self.adresseIP,9999)
        self.mcn.run()

        for i in range(len(Position)):
            xd=Position[i][0]
            yd=Position[i][1]

            self.mcn.updateModelInfo()
            (x,y),theta = self.mcn.getPos2DAndYaw(self.name)

            X=[x]         # Liste permettant de garder toutes les positions du robot
            Y=[y]

            while ((abs(xd-x)>=erreur) or (abs(yd-y)>=erreur)):
                x_tilde = xd - x
                y_tilde = yd - y

                if xd>=x:
                    theta=theta%pi
                    theta_tilde=atan((y-yd)/(x-xd))-theta
                else:
                    theta=theta%pi
                    theta_tilde=atan((y-yd)/(x-xd))-theta+pi

                theta_tilde=atan((y_tilde)/(x_tilde))-theta

                d=sqrt(x_tilde**2+y_tilde**2)
                v = d/(k1 + d) * vmax * cos(theta_tilde)
                w = v/d * sin(theta_tilde) + k2 * tanh(k3 * theta_tilde)
                vd=v+(delta/2)*w
                vg=v-(delta/2)*w

                PWMD=vd/Ks         # commande à envoyer aux roues du robot pendant une durée dt (assez petite) à choisir
                PWMG=vg/Ks

                msg= 'STOP'
                self.client.send(msg)
                msg = "MOVE "+str(PWMD)+" "+str(PWMG)
                self.client.send(msg)

                self.mcn.updateModelInfo()
                (x,y),theta = self.mcn.getPos2DAndYaw(self.name)
                self.position=(x,y)
                self.yaw = theta

                X.append(x)
                Y.append(Y)

                sleep(0.5)

        msg = "STOP"
        self.client.send(msg)
        self.client.fermer()
        self.mcn.stop()


###

rob=RobotLego(adresseIP="100.75.155.131",name="Lego1",nomDeConfig="PC6")
nodes=rob.recupererNoeuds()
rob.commandeRobot(nodes)



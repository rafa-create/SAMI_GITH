def commandeRobot(Positions):     #Positions: liste des positions à récupérer de la partie maths
    erreur=5
    k1=30
    k2=1
    k3=1
    vmax=50
    delta=10
    Ks=0.5

    for i in range(len(Position)):
        xd=Position[i][0]
        yd=Position[i][1]

        #x
        #y                x, y et theta a récupérer en communiquant avec le robot
        #theta

        X=[x]         #Liste permettant de garder toutes les positions du robot
        Y=[y]

        while ((abs(xd-x)>=erreur) or (abs(yd-y)>=erreur)):
            x_tilde = xd - x
            y_tilde = yd - y
            theta_tilde=atan((y_tilde)/(x_tilde))-theta

            d=sqrt(x_tilde**2+y_tilde**2)
            v = d/(k1 + d) * vmax * cos(theta_tilde)
            w = v/d * sin(theta_tilde) + k2 * tanh(k3 * theta_tilde)
            vd=v+(delta/2)*w
            vg=v-(delta/2)*w

            PWMD=vd/Ks         #commande à envoyer aux roues du robot pendant une durée dt (assez petite) à choisir
            PWMG=vg/Ks

            #x
            #y                x, y et theta a récupérer en communiquant avec le robot
            #theta

            X.append(x)
            Y.append(Y)
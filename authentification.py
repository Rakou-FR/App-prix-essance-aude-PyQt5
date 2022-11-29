import bcrypt

def connexion():
    pseudo = input("Pseudo: ")
    mdp = input("mot de passe: ")
    
    if not len(pseudo or mdp) < 1:
        
        bdd = open("main/bdd.txt", "r")
        d = []
        f = []
        for i in bdd:
            a, b = i.split(",")
            b = b.strip()
            d.append(a)
            f.append(b)
            data = dict(zip(d, f))
            
        if pseudo in data:
            hashh = data[pseudo].strip('b')
            hashh = hashh.replace("'", "")
            hashh = hashh.encode('utf-8')
                    
            if bcrypt.checkpw(mdp.encode(), hashh):
                        
                print("Connexion réussie!")
                print("Bonjour", pseudo)
                            
            else:
                print("Mot de passe incorrect")
                connexion()
                        
        else:
            print("Pseudo non existant")
            connexion()

    else:
        print("Veuillez réessayer de vous connecter")
        connexion()
	
  

def inscription():
    pseudo = input("Pseudo: ")
    mdp1 = input("Mot de passe: ")
    mdp2 = input("Confirmation mot de passe: ")
    bdd = open("main/bdd.txt", "r")
    d = []

    for i in bdd:
        a,b = i.split(",")
        b = b.strip()
        d.append(a)

    if not len(mdp1)<=8:
        bdd = open("main/bdd.txt", "r")



        if len(pseudo) <1:
            print("Veulliez entrer un pseudo")
            inscription()

        elif pseudo in d:
            print("Pseudo déjà utilisé")
            inscription()

        else:

            if mdp1 == mdp2:
                mdp1 = mdp1.encode('utf-8')
                mdp1 = bcrypt.hashpw(mdp1, bcrypt.gensalt())              
                bdd = open("main/bdd.txt", "a")
                bdd.write(pseudo+", "+str(mdp1)+"\n")
                print("Nouvel utilisateur crée")
                print("Veuillez vous connecter pour continuer")
                
            else:
                print("Les mots de passe ne correspondent pas")
                inscription()
    
    else:
        print("Mot de passe trop court")



def main():
	print("Veulliez choisir une des deux options")
	choix = input("Connexion | Inscription:")

	if choix == "Connexion":
		connexion()

	elif choix == "Inscription":
		inscription()

	else:
		print("L'option selectionnée est incorrecte, veulliez réessayer...")

main()
import pandas as p

'''
    id: id[text]
    cp: cp[text]
    pop: pop[text]
    adresse: adresse[text]
    ville: ville[text]
    horaires: horaires[text]
    geom: geom[geo_point_2d]
    prix_maj: prix_maj[datetime]
    prix_id: prix_id[text]
    prix_valeur: prix_valeur[double]
    prix_nom: prix_nom[text]
    com_arm_code: com_arm_code[text]
    Nom Officiel Commune / Arrondissement Municipal: com_arm_name[text]
    Code Officiel EPCI: epci_code[text]
    Nom Officiel EPCI: epci_name[text]
    Code Officiel Département: dep_code[text]
    Nom Officiel Département: dep_name[text]
    Code Officiel Région: reg_code[text]
    Nom Officiel Région: reg_name[text]
    Code Officiel Commune: com_code[text]
    Nom Officiel Commune: com_name[text]
    services_service: services_service[text]
    Automate 24-24 (oui/non): horaires_automate_24_24[text]
'''

def recherche():
    f = p.read_csv("sus.csv", delimiter=";", keep_default_na=False)
    tri = f.sort_values(by=["cp"])
    aude = tri[(tri["cp"] >= 11000) & (tri["cp"] < 12000)]
    v_recherche = str(input("Entrez le code postal de votre ville audoise: "))
    
    if len(v_recherche) > 0:
        cp_int = int(v_recherche)
        df = aude[aude["cp"].isin([cp_int])]
        
        if df.size != 0:
            print(df["adresse"])
                        
        else:
            print("Ce code postal n'est pas audois ou ne possède pas de station.")
    
    else:
        print("Veuillez entrer une valeur.")
        
    
recherche()
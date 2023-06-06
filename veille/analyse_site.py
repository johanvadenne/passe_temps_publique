import requests
from bs4 import BeautifulSoup


def ligne_modifier(nom, nouveau_texte):
        
    lignes = ""
    
    fichier = open("contenue_page_temporaire.txt", "r+", encoding="utf-8")
    texte = fichier.readlines()
    fichier.close()
    
    for i in range(len(texte)):
        
        if (texte[i] == "modifier\n"):
            
            if (i+1 not in sites[nom]):
                print("ligne {} modifier".format(str(i+1)))
                lignes += nouveau_texte[i]+"\n"
    
    
    
    # écrie les modification
    fichier = open("modification_site/"+nom+".txt", "w+", encoding="utf-8")
    fichier.write(str(lignes))
    fichier.close()


def comparateur(pages):
    
    # initialize variable
    ancien_text = pages[0]
    nouveau_text = pages[1]
    text = ""
    mofification = False
    lignes = ""
    
    # pour chaque ligne de l'ancien texte
    for ligne in nouveau_text:
        # si elle existe dans le nouveau texte "ok"
        if ligne in ancien_text:
            text += "ok\n"
        # sinon modification détécter
        else:
            text += "modifier\n"
            mofification = True
    
    # écrie le nouveau texte html
    fichier = open("contenue_page_temporaire.txt", "w+", encoding="utf-8")
    fichier.write(str(text))
    fichier.close()
    
    return mofification


def connexion_site():
    
    # Pour chaque site
    for nom, site in sites.items() :
        
        try:
            
            # connexion
            reponse = requests.get(site[0])
            # si la réponse est correct
            if reponse.status_code == 200:
                # affiche le message correct
                print(nom + ": La connexion au site web a réussi.")

            # sinon
            else:
                # affiche le code d'echec
                print(nom + ": La connexion au site web a échoué. Code de statut :", reponse.status_code)

                # retire le nom du site de la liste
                sites.pop(nom)
        
        # si ERREUR
        except requests.exceptions.RequestException as e:
            # affiche l'erreur
            print("Une erreur s'est produite lors de la connexion :", str(e))

            # retire le nom du site de la liste
            sites.pop(nom)

def recupere_texte(nom, site):
    
        # connect au site
        reponse = requests.get(site)
        
        # récupère le text html
        contenue_page = reponse.text
        
        
        # récupère l'ancien text html en form de liste
        fichier = open("sites/"+nom+".txt", "r", encoding="utf-8")
        ancien_contenue_page = fichier.readlines()
        fichier.close()
        
        # écrie le nouveau texte html
        fichier = open("sites/"+nom+".txt", "w+", encoding="utf-8")
        fichier.write(str(contenue_page))
        fichier.close()
        
        # récupère le nouveau text html en forme de liste
        fichier = open("sites/"+nom+".txt", "r", encoding="utf-8")
        contenue_page = fichier.readlines()
        fichier.close()
        
        return ancien_contenue_page, contenue_page



def recupere_lien(nom):
    
    liens = []
    
    # récupère le nouveau text html en forme de liste
    fichier = open("modification_site/"+nom+".txt", "r", encoding="utf-8")
    contenue_modifier = fichier.readlines()
    fichier.close()

    for ligne in contenue_modifier:
        
        if ("<a " in ligne and "href=" in ligne):
            
            # Analyser le code HTML
            soup = BeautifulSoup(ligne, 'html.parser')

            # Récupérer la valeur de l'attribut href
            href = soup.a['href']

            if (href not in liens):
                liens.append(href)
                print(href)

            
    


sites = {
"lemondeinformatique" : ["https://www.lemondeinformatique.fr/", 77, 648, 653, 654, 657, 658, 661, 662, 665, 666, 669, 670, 673, 674],
"clubic" : "https://www.clubic.com/",
"usine-digitale" : "https://www.usine-digitale.fr/",
"zdnet" : "https://www.zdnet.fr/",
"nextinpact" : "https://www.nextinpact.com/",
"generation-nt" : "https://www.generation-nt.com/",
"lesnumeriques" : "https://www.lesnumeriques.com/",
"numerama" : "https://www.numerama.com/",
"fredzone" : "https://www.fredzone.org/",
"presse-citron" : "https://www.presse-citron.net/",
"ginjfo" : "https://www.ginjfo.com/",
"vonguru" : "https://vonguru.fr/",
"journaldugeek" : "https://www.journaldugeek.com/",
"tomsguide" : "https://www.tomsguide.fr/",
"leclaireur" : "https://leclaireur.fnac.com/",
"01net" : "https://www.01net.com/",
"korben" : "https://korben.info/",
"cowcotland" : "https://www.cowcotland.com/",
"futura-sciences" : "https://www.futura-sciences.com/",
"tomshardware" : "https://www.tomshardware.fr/",
"journalducoin" : "https://journalducoin.com/",
"overclocking" : "https://overclocking.com/",
"maison-et-domotique" : "https://www.maison-et-domotique.com/",
"minimachines" : "https://www.minimachines.net/",
"3dvf" : "https://3dvf.com/",
"cachem" : "https://www.cachem.fr/",
"touslesdrivers" : "https://www.touslesdrivers.com/",
"lesmobiles" : "https://www.lesmobiles.com/",
"mac4ever" : "https://www.mac4ever.com/",
"macg" : "https://www.macg.co/",
"frandroid" : "https://www.frandroid.com/",
"macbidouille" : "https://macbidouille.com/",
"iphon" : "https://www.iphon.fr/",
"toolinux" : "https://www.toolinux.com/",
"tablette-tactile" : "https://www.tablette-tactile.net/",
"linuxfr" : "https://linuxfr.org/",
"universfreebox" : "https://www.universfreebox.com/",
"monwindows" : "https://www.monwindows.com/",
"lemagit" : "https://www.lemagit.fr/",
"usinenouvelle" : "https://www.usinenouvelle.com/",
"silicon" : "https://www.silicon.fr/",
"lebigdata" : "https://www.lebigdata.fr/",
"larevuedudigital" : "https://www.larevuedudigital.com/",
"programmez" : "http://www.programmez.com/",
"legalis" : "https://www.legalis.net/",
"zataz" : "https://www.zataz.com/",
"gamekult" : "https://www.gamekult.com/",
"xbox-gamer" : "https://www.xbox-gamer.net/",
"psmag" : "https://www.psmag.fr/",
"jeuxvideo" : "https://www.jeuxvideo.com/",
"p-nintendo" : "https://www.p-nintendo.com/",
"gameblog" : "https://www.gameblog.fr/",
"nofrag" : "https://nofrag.com/",
"factornews" : "https://www.factornews.com/",
"judgehype" : "https://www.judgehype.com/",
"jeuxonline" : "https://www.jeuxonline.info/",
"hdnumerique" : "https://www.hdnumerique.com/",
"allocine" : "https://www.allocine.fr/",
"avcesar" : "https://www.avcesar.com/",
"premiere" : "https://www.premiere.fr/",
"phototrend" : "https://phototrend.fr/",
"ecranlarge" : "https://www.ecranlarge.com/",
"journaldujapon" : "http://www.journaldujapon.com/"
}



#connexion_site()

for nom, site in sites.items() :
    
    contenue_des_page = recupere_texte(nom, site[0])
    if (comparateur(contenue_des_page)):
        ligne_modifier(nom, contenue_des_page[1])
        recupere_lien(nom)
    
    break
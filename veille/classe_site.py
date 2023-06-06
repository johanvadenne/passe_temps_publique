import requests
import os
from bs4 import BeautifulSoup
import historique

liens_historique = historique.historique
liens_historique_sans_http = historique.historique_sans_http

class site_internet:
    
    nom = str
    url = str
    sous_url = list
    news_liens = list
    news_liens_sans_url_http = list

    _nouveau_contenue_page = str
    
    
    def __init__(self, nom_en_cours, url_en_cours, sous_url_en_cours ):
        
        self.nom = nom_en_cours
        self.url = url_en_cours
        self.sous_url = sous_url_en_cours
        self._nouveau_contenue_page = ""
        self.news_liens = []
        self.news_liens_sans_url_http = []
   
        
    
    def _exist(self, lien, dossier = False):
        
        if (not os.path.exists(lien)):

            if (dossier):
                os.mkdir(lien)
            
            else:
            
                fichier = open(lien, "w+", encoding="utf-8")
                fichier.close()
            
        
        
    
    def verifie_fichier_existant(self):
        
        num_sous_lien = 0
        
        self._exist("sites/{}.txt".format(self.nom))
        #self._exist("nouveau_lien/{}.txt")
        
        for num_sous_lien in range(len(self.sous_url)):

            
            self._exist("sites/{}".format(self.nom), True)
            #self._exist("nouveau_lien/{}".format(self.nom), True)
            
            nom_sous_lien = "/sous_lien_"+str(num_sous_lien)+".txt"
            
            self._exist("sites/{}".format(self.nom+nom_sous_lien))
            #self._exist("nouveau_lien/{}".format(self.nom+nom_sous_lien))
            
            
    
    
    def connexion_site(self):
        
        
        try:
            reponse = requests.get(self.url)
            if reponse.status_code == 200:
                print(self.nom + ": La connexion au site web a réussi.")
                connexion = True

            else:
                print(self.nom + ": La connexion au site web a échoué. Code de statut :", reponse.status_code)
                connexion = False

        
        except requests.exceptions.RequestException as e:

            print("Une erreur s'est produite lors de la connexion :", str(e))
            connexion = False
        
        return connexion
    
    
    
    def recupere_page_html(self, sous_lien = ""):
        
        
        reponse = requests.get(self.url)
        
        self._nouveau_contenue_page = reponse.text
        
        
    def extrait_lien(self, nom_sous_lien = "", lien = ""):
                
        # Analyser le code HTML
        soup = BeautifulSoup(self._nouveau_contenue_page, 'html.parser')

            # Récupérer la valeur de l'attribut href
        a = soup.find_all('a')

        for tag  in a:

            try:

                href = tag.get('href')

                if ("#" in href):

                    href = href.split("#")[0]

                if (href not in self.news_liens and href not in self.news_liens_sans_url_http and href not in liens_historique_sans_http and href not in liens_historique):

                    if ("http://" in href or "https://" in  href):
                        self.news_liens.append(href)
                    else:
                        self.news_liens_sans_url_http.append(href)
                        href = lien + href
                        self.news_liens.append(href)
        
            except:
                continue

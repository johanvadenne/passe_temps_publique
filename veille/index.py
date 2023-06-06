import classe_site
import variable_globale
import pprint
import historique
import asyncio

liens_historique = historique.historique
liens_historique_sans_http = historique.historique_sans_http
liens_news = {}

for nom_site, info_site in variable_globale.sites.items():

    liens = []
    liens_sans_http = []
    
    site = classe_site.site_internet(nom_site, info_site[0], info_site[1])
    
    
    print()

    if (site.connexion_site()):

        try:
        
            site.recupere_page_html()
            site.extrait_lien("", site.url)

            num_sous_lien = 0

            liens.extend(site.news_liens)
            print(site.url)
            #pprint.pprint(site.news_liens)
        
        except:
            print("erreur: 1")

        for sous_lien in site.sous_url:

            try:

                nom_sous_lien = "/sous_lien_"+str(num_sous_lien)

                site.recupere_page_html(nom_sous_lien)
                site.extrait_lien(nom_sous_lien, sous_lien)
                num_sous_lien += 1

                liens.extend(site.news_liens)
                liens_sans_http.extend(site.news_liens_sans_url_http)
                print(sous_lien)
                #pprint.pprint(site.news_liens)

            except:
                print("erreur: 2")


        liens_sans_doublons = list(set(liens_sans_http))
        liens_historique_sans_http.extend(liens_sans_doublons)

        liens_sans_doublons = list(set(liens))
        liens_historique.extend(liens_sans_doublons)
        liens_news[site.nom] = liens_sans_doublons

pprint.pprint(liens_news)

liens_historique = list(set(liens_historique))
fichier = open("historique.py", "w+", encoding="utf-8")
fichier.write("historique = "+str(liens_historique)+"\n\nhistorique_sans_http = "+str(liens_historique_sans_http))
fichier.close
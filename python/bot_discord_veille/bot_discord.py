# This example requires the 'message_content' privileged intent to function.

import discord
import classe_site
import variable_globale
import pprint
import historique

salons = {
"jeuxonline":  "id_canal",
"cowcotland":  "id_canal",
"touslesdrivers":  "id_canal",
"fnac": "id_canal",
"tomshardware":  "id_canal",
"techdows":  "id_canal",
"jeuxvideo":  "id_canal",
"linuxfr":  "id_canal",
"programmez":  "id_canal",
"silicon":  "id_canal",
"ginjfo":  "id_canal",
"nextinpact":  "id_canal",
"zataz":  "id_canal",
"allocine":  "id_canal",
"journalducoin":  "id_canal",
"xbox-gamer":  "id_canal",
"journaldujapon":  "id_canal",
"usinenouvelle":  "id_canal",
"lemondeinformatique":  "id_canal",
"monwindows":  "id_canal",
"3dvf":  "id_canal",
"psmag":  "id_canal",
"usine-digitale":  "id_canal",
"frandroid":  "id_canal",
"gameblog":  "id_canal",
"tomsguide":  "id_canal",
"minimachines":  "id_canal",
"generation-nt":  "id_canal",
"presse-citron":  "id_canal",
"futura-sciences":  "id_canal",
"gamekult":  "id_canal",
"p-nintendo":  "id_canal",
"hdnumerique":  "id_canal",
"journaldugeek":  "id_canal",
"premiere":  "id_canal",
"toolinux":  "id_canal",
"korben":  "id_canal",
"fredzone":  "id_canal",
"maison-et-domotique":  "id_canal",
"tablette-tactile":  "id_canal",
"mac4ever":  "id_canal",
"universfreebox":  "id_canal",
"larevuedudigital":  "id_canal",
"lebigdata":  "id_canal",
"numerama":  "id_canal",
"legalis":  "id_canal",
"clubic":  "id_canal",
"cachem":  "id_canal",
"macg":  "id_canal",
"lesmobiles":  "id_canal",
"factornews":  "id_canal",
"ecranlarge":  "id_canal",
"iphon":  "id_canal",
"avcesar":  "id_canal",
"lemagit":  "id_canal",
"zdnet": "id_canal",
"overclocking":  "id_canal",
"vonguru": "id_canal",
"lesnumeriques":  "id_canal",
"01net":  "id_canal",
"macbidouille":  "id_canal"
}

async def action(self, message):
    liens_historique = historique.historique
    liens_historique_sans_http = historique.historique_sans_http
    liens_news = {}

    for nom_site, info_site in variable_globale.sites.items():

        liens = []
        liens_sans_http = []
        liens_sans_doublons = []

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


        salon = client.get_channel(salons[nom_site])
        if salon:
            for lien in liens_sans_doublons:
                await salon.send(str(lien))
        


    pprint.pprint(liens_news)
    
    liens_historique = list(set(liens_historique))
    fichier = open("historique.py", "w+", encoding="utf-8")
    fichier.write("historique = "+str(liens_historique)+"\n\nhistorique_sans_http = "+str(liens_historique_sans_http))
    fichier.close


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!news'):
            await message.reply("C'est partie!", mention_author=True)
            await action(self, message)
        
        if message.content.startswith('!good bye'):
            await message.reply("bye bye 👋!", mention_author=True)
            await client.close()
            
            


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('token_bot')
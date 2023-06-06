SLAM1 - B1 (Système) - Cahier de texte - 2022-2023  
Pierre TESSONNEAU
===


1. **Cours Active Directory**
   - [Introduction Active Directory](https://www.youtube.com/watch?v=qf4OtEBu9vA)
   - [Contrôleur de domaine](https://www.youtube.com/watch?v=lO6NviXHwIk)

> Ressources complémentaires :
> - https://openclassrooms.com/fr/courses/2222496-centralisez-et-securisez-votre-annuaire-active-directory
> - https://openclassrooms.com/fr/courses/7723396-assurez-la-securite-de-votre-active-directory-et-de-vos-domaines-windows


2. **TP Active Directory**
   - Copier le fichier **clone srv-2019.vdi** en local (sur D: par exemple)
   - Créer une une nouvelle machine virtuelle sous VirtualBox
      - Nouvelle machine
      - Choix du répertoire de destination
      - Mémoire 2GB
      - Type machine : other windows 64
      - Importer à partir de VDI
      - Password: Azertysio-01
   - Suivre les étapes du TP : **TP Active Directory sous Windows.doc**
      - En vous aidant des documents fournis
      - [Tutoriels](https://www.youtube.com/playlist?list=PLZ_TUwoqPyUWJqISB0xtzX20hjwLL-Dqz)
      -  Paramétrer les @IP avec les plages d'adresses affectées (remplacer XXX par votre adresse perso)
         - Machine physique :
            - @IP : 172.16.XXX.1
            - Masque : 255.255.0.0
            - Passerelle : 172.16.0.1
            - DNS : 8.8.8.8
         - VM Windows server
            - @IP : 172.16.XXX.10
            - Masque : 255.255.0.0
            - Passerelle : 172.16.0.1
            - DNS : 127.0.0.1
      - Dans virtual box :
         - Configuration/Réseau/Mode accès réseau : "accès par pont"


>TODO  : Rapport **TP Active Directory**
>  - Pour chaque question :
>     - Reporter le numéro de la question
>     - Donner la solution (copie d'écran,...)


3. Correction BTS Blanc

# Jeudi 08/12/2022

* TP : TP-SMB01_Linux.docx (A finir)
   
# Jeudi 01/12/2022

* Protocole SMB (SAMBA)
  * TP : TP-SMB01_Windows.docx (FIN)
    * Prendre la VM windows_10_21h2_x64.ova pour le TP (sio / Azertysio-01)
    * Pour la partie linux : prendre la VM Debian 11.5 (sio / azertysio)

* TP : TP-SMB01_Linux.docx
    * Prendre la VM Debian 11.5 (sio / azertysio) pour 1 CLIENT et 1 SERVEUR
  

# Mardi 29/11/2022

* Gestion des utilisateurs et des droits
   * TP : TP Authentification, autorisation et journalisation_MAJ.pdf (Fin)

>Ce TP montre comment gérer les accès aux différentes ressource d'un Système d'Information à l'aide **d'une politique de sécurité**.
>
>**Le principe de classification de l'information** : un procédé de classification de l’information idéal reflétera l’activité de l’entreprise. Concevez votre procédé en fonction de la sensibilité, de la valeur et de l’importance stratégique de vos données, ainsi que des exigences légales, afin de pouvoir protéger chaque actif de manière appropriée.
>La plupart des entreprises commencent avec trois ou quatre catégories seulement. 
>   * __Très restreint__ – Nécessite des mesures de sécurité importantes ainsi qu’un accès strictement contrôlé et limité.
>   * __Restreint__ – Nécessite des mesures de sécurité assorties d’un accès limité mais peu important et non strictement contrôlé.
>   * __Utilisation interne__ – Ne nécessite pas de protection supplémentaire.
Exemple de procédé de classification à quatre catégories : confidentiel, restreint, interne et public.

> La **gestion des droits d'accès ou gestion d'identité** assure aux organisations que seuls les utilisateurs autorisés ont accès à leurs données. Cela permet notamment de diminuer les risques d'intrusions et d'attaques ainsi que de protéger l'intégrité de leurs données.
 


# Lundi 28/11/2022

* Gestion des utilisateurs et des droits
  * Prendre connaissance du document "Administration des utilisateurs.pdf"
  * TP : TP Authentification, autorisation et journalisation_MAJ.pdf
    * * Prendre la VM Ubuntu_20.04.4_SIO.ova


# Jeudi 24/11/2022

* Protocole SMB (SAMBA)
  * [Vidéo introduction](https://www.youtube.com/watch?v=j9ychSUygBI&ab_channel=IT-Connect)
  * TP : TP-SMB01_Windows.docx
    * Prendre la VM windows_10_21h2_x64.ova pour le TP (sio / Azertysio-01)
    * Pour la partie linux : prendre la VM Debian 11.5 (sio / azertysio)
  

# Vendredi 18/11/2022
_Pas cours (jour férié)_



# Mardi 15/11/2022 (Echange cours B3 avec vendredi 18/11/2022)
* Evaluation : Quiz Système Linux

> IANA : [Liste des ports IANA](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)



# Lundi 14/11/2022 (Echange cours B3 avec vendredi 18/11/2022)
* Rappel : Docs UNIX
  * UNIX_commandes-base.pdf
  * UNIX_gnu-linux.pdf
  * UNIX_shells.pdf

* Système d'exploitation : 
   *  TP-OS4 Demarrer avec une debian linux-suite
      *  Identifiant : root
      *  Mot de passe : azertysio

TODO : 
   -  Pour le 15/11/2022 : 
      -  Déposer le CR du TP (TP0S4 Debian suite) dans le dépot, renommé SLAM1-B1-TP0S4-Dabian-suite_NomPrénom.pdf
      -  Réviser les cours/TP linux


# Vendredi 11/11/2022
_Pas cours (jour férié)_


# Vendredi 21/10/2022
* Docs UNIX
  * UNIX_commandes-base.pdf
  * UNIX_gnu-linux.pdf
  * UNIX_shells.pdf

* Système d'exploitation : 
   *  TP-OS3 Demarrer avec une debian linux (SUITE)
      *  Identifiant : sio
      *  Mot de passe : azertysio

TODO : 
   -  Pour le 28/10/2022 : Finir le TP linux et envoyer le Compte rendu nommé SLAM1-B1-TP-OS3-Linux_NomPrénom.pdf par EcoleDirect (par message car le dépot n'est pas possible sur des dates de vacances)

>Infos : 
>- Pour les absents vous pouvez récupérer la Machine Virtuelle sur le réseau
>- Question 7 : il faut chercher les nom de fichiers FINISSANT par 'conf'
>- Pour la configuration réseau, il faut remplacer 172.16.XX.XX par l'adresse que vous souhaitez mettre à votre machine virtuelle Debian
>  - Exemple si votre ordinateur est en 172.16.140.1 vous allez mettre 172.16.140.2
>  - Pour connaitre votre adresse IP : **ipconfig** dans l'invité de commande de Windows
>  - Attention le caractère # permet de mettre en commentaire la ligne du ficher de conf.
>  Faire attention, il y a des lignes à mettre en commentaire.



# Jeudi 13/10/2022
* Système d'exploitation : 
   *  TP-OS3 Demarrer avec une debian linux
      *  Identifiant : sio
      *  Mot de passe : azertysio

TODO : 
   - Compte rendu nommé SLAM1-B1-TP-OS3-Linux_NomPrénom.pdf à déposer dans PARTAGE

# Jeudi 06/10/2022
 * Système d'exploitation : 
   * TP A la découverte d'un OS

TODO : 
   - Renommer le ficher : SLAM1-B1-TP-OS_NomPrénom.pdf
   - Déposer le fichier dans Y:\PARTAGE\01-B1\TP04-OS\


# Jeudi 29/09/2022
Cours annulé.

# Jeudi 22/09/2022

1. Le système d'exploitation :
   - Cours : ```Le système d'exploitation.pdf```
   - TP : ```TP Virtual box.pdf```
      - Si problème à l'installation de Win10, désactiver USB ou metre USB en 1.1

> **Fichier ISO** : Un fichier ISO est, en termes simples, un format de fichier numérique reproduisant un CD, un DVD ou un BD physique. L'extension de fichier ISO ne se contente pas de stocker des fichiers et des dossiers : elle contient toutes les informations vitales du système de fichiers concernant la structure du disque.

> Les fichiers avec l'extension .VDI contiennent des images de disque virtuel ainsi que des métadonnées associées. VDI est le format d'image natif de VirtualBOX, un logiciel de virtualisation de système. 

> **Fichier OVA** : Le .ova extension de fichier est joint à des fichiers qui contiennent des descriptions d'une machine virtuelle.

TODO: Rechercher comment faire les derniers points du TP :
   - Faire un instantané
   - Cloner une VM
   - Gestion d’un dossier partagé
   - Exporter dans le format OVA


# Jeudi 15/09/2022

1. Environnement de travail (rappel)
   - Nommer et classer ses documents
   - Extension de fichiers sous Windows

2. Activité : Monter (virtuellement) son PC 
   
   En vous aidant du TP01 de la semaine dernière, simuler un achat de PC complet, composant par composant :
   - Aller sur le site [topachat.com](https://www.topachat.com/accueil/index.php)
   - Ajouter les composants PC nécessaire dans votre panier
   - Imprimer en PDF le contenu de votre panier et sauvegarder en PDF : 
  ```SLAM1-B1-Activité-TopAchat_NOM-Prénom.pdf```

  3. Cours : ```02-B1-CPU-Bus-RAM.pdf``` (Partie 1 : CPU)

TODO: Lire la fin du cours.


# Jeudi 08/09/2022

1. Cours : Présentation Bloc B1 (Partie Système) ```01-B1-Présentation.pdf```

2. TP01 - Composants PC
   -  Renommer le fichier : SLAM1-B1-TP01_NOM-Prénom.pdf
   -  Compléter le fichier 
   -  Le déposer dans \\SLAM1\PARTAGE\\01-B1\01-TP1
   -  Correction du TP
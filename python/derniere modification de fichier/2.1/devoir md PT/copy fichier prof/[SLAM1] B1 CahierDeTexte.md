SLAM1 - B3 - Cahier de texte - 2022-2023  
Pierre TESSONNEAU
===

# Lundi 21/11/2022

* TD 2.1 - Préserver l’identité numérique de l’organisation

* Protocole FTP / SFTP, notion de chiffrage, différence entre chiffrage / Cryptage

TODO: Révision pour Quiz du lundi 28/11/2022
   - Telnet
   - Protocole FTP / SFTP, notion de chiffrage, différence entre chiffrage / Cryptage
   - schéma Modèle OSI


# Lundi 21/11/2022

* TP Labtainer : telnetlab (FIN)


# Vendredi 18/11/2022

* Mise en place de **Labtainer**
   * Télécharger la VM pour VirtualBox [ici](https://nps.edu/web/c3o/virtual-machine-images)
   * Importer la VM dans Virtualbox
   * Lancer la VM
      > L’authentification sur la machine virtuelle labtainer se fait avec **student**, mot de passe **password123**. Comme la VM est en clavier qwerty, il faudra taper **pqsszord&é** ou **pqsszord123** si vous disposez d’un pavé numérique sur votre clavier.

      >NB : la VM est en qwerty. Pour mettre le clavier en français, il faut désormais utiliser l'assistant graphique (cf [article](https://www.clubic.com/tutoriels/article-862595-1-comment-clavier-qwerty-azerty-ubuntu.html)).
 
   * Mettre à jour la VM
      * Mettre à jour votre installation Labtainers (labs fix)  en exécutant : ```update-labtainer.sh``` à partir de votre répertoire labtainers-student.

   *  Démarrer et stopper un lab : 
      *  ```labtainer <NomLab>```
      *  ```stoplab <NomLab>```


* Cours TELNET
  
* TP Labtainer : telnetlab

> Références réseau : [FrameIP](https://www.frameip.com/tcpip/)


# Mardi 19/10/2022

* TD 1.3.1 - La réglementation

* Exposé Cyberattaques
   - Téléchargement furtif : Maxime et Noé
   - DDOS : Marius et Camille

* Actualités : [Vidéo : Cyber la guerre est déclarée](https://www.france.tv/france-5/c-dans-l-air/4145386-cyber-la-guerre-est-declaree.html)



TODO:
Pour le **mardi 8 novembre** : 
  
   - Résumé vidéo : Faire un résumé sur demi-page A4 de la vidéo : replay france TV : https://www.france.tv/france-5/c-dans-l-air/4145386-cyber-la-guerre-est-declaree.html
      (Pour les apprentis: vous pouvez visualiser la vidéo également mais je ne demande pas de résumé).
      Renommer le ficher SLAM1-AP-RésuméVidéo_NomPrénom.pdf à déposer dans le dépot EcoleDirecte en PDF.
  
   
# Mardi 11/10/2022

* Exposé Cyberattaques
   - MITM : Jules
   - Cassage de mots de passe : Johan

* TD 1.3.1 - La réglementation


# Lundi 10/10/2022

*  TD 1.2 Principes de la sécurité : Critères DCIP


# Mardi 04/10/2022

*  Evaluation THEME 1 - La protection des données à caractère personnel

*  TD 1.2 Principes de la sécurité (DEBUT)


# Lundi 03/10/2022

1. Sureté / Sécurité
   - [Introduction en vidéo](https://www.youtube.com/watch?v=JLP13i2MZg4&ab_channel=Inria)
   - TD 1.4
     - Sécurité et sûrete

      ><span style="color: #26B260">
      >
      > - La **sécurité** : Traite les problèmes liés aux actes malveillants.
      > - La **sûreté** : se préoccupe de la continuité et de la qualité de service, de la capacité à résister à un événement accidentel.
      ></span>

     - Les types de menaces

      ><span style="color: #26B260">
      > L’ANSSI définit aussi quatre principaux types de menaces :
      > 
      > - **Déstabilisation** : Les attaquants cherchent à déstabiliser leur victime, à nuire à son image.
      > - **Espionnage** : les attaquants cherchent à infiltrer le réseau de la victime (par exemple grâce à un virus…) afin de l’espionner.
      > - **Sabotage** : les attaquants cherchent à créer une panne dans le Système d’information de la victime.
      > - **Cybercriminalité** : les attaquants poursuivent un but criminel afin souvent d’obtenir de l’argent. Par exemple : rançongiciel (ransomware), phishing (hameçonnage).
      > </span>

  

# Mardi 27/09/2022

1. Méthodologie d'analyse de risque de l'ANSSI : l'EBIOS Risk Manager 
   - TD 1.3 La méthode EBIOS

      ><span style="color: #26B260">
      >
      > **EBIOS** : (Expression des besoins et identification des objectifs de sécurité)
      > Méthode de référence :
      > - développée par l'Agence nationale de la sécurité des systèmes d'information (ANSSI),
      > - qui permet aux organisations de réaliser une appréciation et un traitement des risques, en fonction de leur contexte.
      </span>

<span style="color: red; background-color: pink">  
TODO: 
  - Pour le 04/10/2022 : Devoir surveillé sur le vocabulaire.
  - Pour le 10/10/2022 : Exposé Cyberattaques.
</span>


# Lundi 26/09/2022

1. Actualité cyber : attaque d'un hopital
   - https://www.tf1.fr/tf1/jt-we/videos/cyberattaque-a-lhopital-des-informations-confidentielles-divulguees-84848728.html

2. Précisions sur l'exposé cyberattaque
   - Mise à jour du TP : ```TP-Exposé-Cyberattaques-V1.2.pdf```
   
   - Complément de cours [CyberEdu : Sensibilisation et initiation à la cybersécurite](https://www.ssi.gouv.fr/uploads/2016/05/cyberedu_module_1_notions_de_base_02_2017.pdf)
        - Notions de critères DIC
        - Panorama de quelques menaces

3. TD 1.2 Les risques liés aux données à caractère personnel suite
   - Définitions

      ><span style="color: #26B260">
      > 
      > **Vulnérabilité** : Faiblesse au niveau d’un bien (au niveau de la conception, de la réalisation, de l’installation, de la configuration ou de l’utilisation du bien).
      >
      > **Menace** : Cause potentielle d’un incident, qui pourrait entrainer des dommages sur un bien si cette menace se concrétisait.
      > 
      > **Risque** : c’est la probabilité que soit exploité une vulnérabilité du SI par une menace.
      > 
      > __CRITERES D.I.C.permettant de définir le niveau de sécurité d'un bien du S.I. (Système d'Information)__ :
      > 
      >**Disponibilité** : Propriété d'accessibilité au moment voulu des biens par les personnes autorisées (i.e. le bien doit être disponible durant les plages d’utilisation prévues)
      > 
      > **Intégrité** : Propriété d'exactitude et de complétude des biens
      et informations (i.e. une modification illégitime d’un bien doit pouvoir être détectée et corrigée)
      > 
      > **Confidentialité** : Propriété des biens de n'être accessibles qu'aux personnes autorisées.
      >
      >__1 critère complémentaire est souvent associé au D.I.C.__ : 
      > 
      > **Preuve** : Propriété d'un bien permettant de retrouver, avec
      une confiance suffisante, les circonstances dans lesquelles ce bien évolue. Cette propriété englobe : Notamment :
      >- La traçabilité des actions menées
      >- L’authentification des utilisateurs
      >- L’imputabilité du responsable de l’action effectuée.
      </span>


# Mardi 20/09/2022

1. TD 1.1 Les risques liés aux données à caractère personnel
   - Introduction / généralités
   - Présentation rapide de la CNIL
   - Sécurité des mots de passe : https://www.cnil.fr/fr/mot-de-passe

> **LA CNIL** : 
> La Commission Nationale de l'Informatique et des Libertés (CNIL) a été créée par la loi Informatique et Libertés du 6 janvier 1978.
>
>Elle est chargée de veiller à la protection des données personnelles contenues dans les fichiers et traitements informatiques ou papiers, aussi bien publics que privés.
>
>Ainsi, elle est chargée de veiller à ce que l'informatique soit au service du citoyen et qu'elle ne porte atteinte ni à l'identité humaine, ni aux droits de l'homme, ni à la vie privée, ni aux libertés individuelles ou publiques.
>
>La CNIL est une autorité administrative indépendante (AAI), c'est-à-dire un organisme public qui agit au nom de l'Etat, sans être placé sous l'autorité du gouvernement ou d'un ministre. Elle est composée de 18 membres élus ou nommés et s'appuie sur des services.
>
>Elle a un rôle d'alerte, de conseil et d'information vers tous les publics mais dispose également d'un pouvoir de contrôle et de sanction.

> <span style="color: #26B260">**Donnée personnelle** : Ce sont des informations relatives à une personne physique, qui permettent son identification directe ou indirecte. Ex : directe : nom, prénom, adresse, adresse mail, n° de tél, adresse IP, n° carte bleue, empreinte digitale (+  données biométriques)
Indirecte : coordonnées GPS… </span>

> <span style="color: #26B260">**Les données sensibles** : Ce sont des informations qui révèlent la prétendue origine raciale ou ethnique, les opinions politiques, les convictions religieuses ou philosophiques ou l'appartenance syndicale, ainsi que le traitement des données génétiques, des données biométriques aux fins d'identifier une personne physique de manière unique, des données concernant la santé ou des données concernant la vie sexuelle ou l'orientation sexuelle d'une personne physique. </span>

> <span style="color: #26B260">**Traitement des données personnelles** : C’est une opération (ou un ensemble d’opérations) portant sur des données personnelles, quel que soit le procédé utilisé : Collecte, stockage,
modification, consultation, utilisation, ...</span>

> <span style="color: #26B260">**Base de données** : C’est l’espace de stockage numérique où sont enregistrées les données (la plupart du temps sur un serveur informatique).</span>


# Lundi 19/09/2022
1. TP01 : Introduction à la Cybersécurité2.pdf (Suite)

<span style="color: red; background-color: pink">  
TODO: 
  - Pour le 20/09/2022 : Finir le MOOC ANSII (Unité 1 Module 2)
  - Pour le 10/10/2022 : Exposé Cyberattaques.
</span>

# Mardi 13/09/2022

1. TP02 : Exposé-Cyberattaque-V1.1.pdf

> Conseil diaporama
>     - https://fr.wikiversity.org/wiki/Diaporamas/R%C3%A8gles_d%E2%80%99utilisation


# Lundi 12/09/2022

1. Introduction générale
   - Code de la route
   - Règles sanitaires
   - Sécurité
   - Cybersécurité

2. Cours :
   - 01-B3-Présentation Cybersécurité.pdf
   - 02-B3-Introduction Cybersécurité.pdf

3. TP01 : Introduction à la Cybersécurité.pdf
   - Découverte de l'ANSII
   - MOOC ANSII (Unité 1 Module 1)

TODO:  Finir MOOC ANSII (Unité 1 Module 1).




   


  







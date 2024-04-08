🟢: fait
🟠: en cours
🔴: non fait
## quelle système de gestion de base de données relationnelle (SGBDR)?🟢
Nous utilisons MariaDB.
## Pourquoi avoir choisi cette SGBDR?🟢
Nous avons choisi cette SGBDR afin de faciliter la réalisation des travaux pratiques du cursus scolaire. De plus, pour permettre le déploiement de l'application 24h/24h, nous disposons de machines virtuelles mises à notre disposition par nos professeurs. À ce jour, MariaDB est la seule SGBDR que nous connaissons sur Linux, et pour le projet en cours de développement, il n'est pas nécessaire de se poser davantage de questions. Nous sommes contraints par le temps et ne pouvons pas consacrer plus de temps à cette décision.
## Quel langage utiliser ?🟢
Nous utilisons MySQL.
## Pourquoi ce langage ?🟢
MariaDB offre une compatibilité avec plusieurs langages SQL, mais le langage par défaut proposé est MySQL. MySQL convient parfaitement à nos besoins, et notre projet n'est pas suffisamment vaste pour susciter un débat sur ce choix. De plus, MariaDB s'assure d'être à jour en fonction des mises à jour de MySQL.
## où ?🟠
- Création du fichier "MACHINE JOHAN sécurité et question" en cours...
- Où se situe la base de données ?
- est-elle en sécurité ?
## Base de données
- **Environnements distincts** :   Les bases BugSafari_TEST, BugSafari_DEV et BugSafari_PROD ont été mises en place, et chacune d'entre elles n'affecte en aucun cas les autres.🟢
-  **Masquage des données** : Le masquage des données n'est pas nécessaire car nous ne transférons ni ne dupliquons aucune de nos trois bases. De plus, les données sensibles et personnelles sont chiffrées, et les mots de passe sont hachés. Le reste de nos données sera en open source, à l'exception de celles qui n'ont aucun intérêt à être rendues publiques.🟢
- **chiffrement et hache**: La méthode de chiffrement reste à définir, mais nous pouvons confirmer que toutes les informations sensibles et personnelles seront chiffrées, et les mots de passe seront hachés. Et pour le moment nous utilisons le hachage sha1🟢
- **Prévention des injections SQL** : À cet effet, nous utilisons des requêtes préparées en PHP, nécessitant une veille sur ce langage.🟢
- **Construction robuste des tables** : Nos tables sont élaborées avec soin par nos experts et vérifiées par des spécialistes. Étant donné la taille limitée de notre projet, toute modification de notre base de données s'effectue rapidement.🟢
- **Gestion des erreurs**: Nous maximisons la gestion des erreurs afin de corriger rapidement toute erreur survenue.🟠
## Sauvegarde
### Type de sauvegarde:
- quelle type de sauvegarde? tout les combiens de temps ?
  Étant donné la petite taille de notre projet en phase de développement, nous effectuons actuellement des sauvegardes complètes toutes les 2 heures. Toutefois, si le projet évolue et prend de l'ampleur, cette question sera sujet à rediscuter.🟢
### log🔴
-  Nous prévoyons de tracer chaque connexion à la base de données, ainsi que chaque requête effectuée sur des tables spécifiques (par exemple, T_Utilisateur). De plus, nous collecterons l'adresse IP publique, l'adresse IP locale, la position, la date (année/mois/jour), l'heure (heure:minute:seconde), et indiquerons si l'action a généré une erreur ou non.
### Quelle est le temps de conservation des sauvegardes ? 
- Nous avons l'intention de conserver nos sauvegardes pendant une période de 6 mois à 1 an, conformément aux recommandations de la CNIL. Tous les 6 mois, nous analyserons les journaux de ces derniers mois afin d'améliorer nos systèmes, puis nous les supprimerons pour éviter d'encombrer notre espace de stockage.🟢
### où ?🟠
- Pour le stockage des sauvegardes, nous prévoyons de les conserver sur une machine voisine, celle de Maxime, en simulant qu'elle ne soit pas dans le même réseau.
  Création du fichier "MACHINE MAXIME sécurité et question" en cours...
## Version
- Nous avons l'intention de créer un programme en tâche cron qui générera un compte rendu du SGBDR ainsi que de ses extensions existantes.🔴
## mettre en place des alertes
- La configuration des alertes sera élaborée sur la machine de Maxime, étant donné qu'elle stocke les sauvegardes ainsi que les journaux.🔴
## Gestion des privilèges🟢
- La gestion des privilèges est minutieusement étudiée pour chaque utilisateur créé.
## Déclaration à la CNIL🔴
- Comme nous traitons des données sensibles et personnelles, nous avons l'intention de faire une déclaration à la CNIL dans les plus brefs délais.
## Mise à jour
- Comment je fais pour vérifier si ma SGBDR est elle à jour ?
  Nous instaurerons un système de veille pour suivre les actualités de MariaDB et de ses extensions.🔴
- comment est-ce que je mis prendre pour ne pas impacter la disponibilité de mon projet ?
  Si le temps le permet, nous envisagerons la création d'une seconde base de données et machine qui prendra le relais afin de maintenir la disponibilité de notre application.🔴
## Test🔴
- Des programmes personnalisés seront développés par nos développeurs afin de tester notre base de données et générer des comptes rendus.
## Documentation détaillée🟢
- Est ce si je pars mon prédécesseur pourra reprendre la main sans aucune difficulté ?
  Nous nous efforçons de maintenir nos documents à jour et de les détailler autant que possible.
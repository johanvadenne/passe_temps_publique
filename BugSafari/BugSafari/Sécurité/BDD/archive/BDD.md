## Base de données
- **[[Environnements distincts]]:** La création de bases de données distinctes pour les environnements de **test**, **développement** et **production**. ✔
- **[[Masquage des données]] :** Pour les environnements de **test** et de **développement**, envisagez de **masquer** ou d'**anonymiser les données sensibles** pour éviter toute divulgation non intentionnelle. ✔
- [[chiffrer la base de données]]: [[Nous utiliserons le chiffrement applicatif]]✔
- **[[Contrer les injections SQL]]** ✔
- Bonne construction des table ✔
## Sauvegarde
### données❌
**Type de sauvegarde:**
- Une **sauvegarde complète** est, comme son nom l’indique, une copie de toutes vos données, de l’ensemble de la base de données ou de l’instance de base de données.
- On parle de **sauvegarde incrémentale** lorsque seules les données modifiées depuis la dernière sauvegarde sont mises à jour dans un nouveau fichier de sauvegarde. Par exemple, si le service comptabilité enregistre trois nouvelles transactions, elles seules seront copiées dans une nouvelle sauvegarde des fichiers de comptabilité.
- Une **sauvegarde différentielle** permet de sauvegarder tous les fichiers qui ont été modifiés depuis la dernière sauvegarde complète.
### log❌
- quelle action ? (connexion, modification, affichage)
- qui ? (ip local, ip publique)
- quand ? (année/mois/jour heure:min:sec)
### Politique de conservation❌
- Établissez une politique de conservation des sauvegardes pour déterminer la durée pendant laquelle les sauvegardes doivent être stockées. Cela peut être influencé par les exigences réglementaires et la criticité des données.
## [[Données sensibles et personnelles]]✔
- hacher ou chiffrer
## alerte❌
- espace stockage
- activités suspectes
- erreur de traitement
## [[Gestion des privilèges]]
- connexion root que si nécessaire✔
- créer des utilisateurs avec les privilèges adaptés✔
## Autre
- quelle système (Windows, Linux, etc)❌
- quelle base de donnée (SQL Server, mariadb, etc)❌
- quelle version de chaque outil et systèmes utiliser?❌
- Documentation détaillée✔
- Déclaration à la CNIL❌
- aucun mot de passe en claire dans le code (sauf les fichier PHP, limiter et optimiser au max!!!)✔
- Mise à jour des outils❌
## Le chiffrement Data-at-Rest
Le principe est de chiffrer les données sur disque, pour se prémunir du vol de fichiers, à travers la solution [InnoDB Data-at-rest Encryption](https://dev.mysql.com/doc/refman/8.0/en/innodb-data-encryption.html) en édition communautaire, ou [Transparent Data Encryption](https://www.mysql.com/products/enterprise/tde.html) (aka **TDE**) en édition Enterprise.

Que ce soit InnoDB Data-at-rest ou TDE, seul le [[tablespace]] est chiffré. Lorsqu’il est lu depuis le disque, MySQL le déchiffre et ensuite son contenu est visible en clair :  
– Depuis le serveur MySQL lui-même.  
– Sur le réseau entre le client et le serveur.  
– Dans l’application.
![[Pasted image 20231130101711.png]]

On comprend donc que l’effet de TDE est limité : il faudra en plus songer à gérer le droit d’en connaître des utilisateurs, chiffrer la communication entre le client et le serveur

# Le chiffrement Data-at-Rest

## Erreurs à Éviter 
Lors de la mise en œuvre du chiffrement avec LUKS, voici quelques erreurs à éviter :

1. **Chiffrement de la Mauvaise Partition :** Assurez-vous de sélectionner la bonne partition à chiffrer. Chiffrer la mauvaise partition peut entraîner la perte de données.

2. **Oubli de Sauvegarde :** Avant de commencer le processus de chiffrement, assurez-vous d'avoir une sauvegarde récente de toutes les données importantes sur la partition. Le processus de chiffrement implique généralement la création d'une nouvelle structure de stockage, et une sauvegarde est une précaution importante.

3. **Perte de la Phrase de Passe :** La phrase de passe est essentielle pour déverrouiller la partition chiffrée. Assurez-vous de vous souvenir de cette phrase de passe ou stockez-la de manière sécurisée. La perte de la phrase de passe peut rendre vos données inaccessibles.

4. **Erreur dans la Syntaxe des Commandes :** Assurez-vous de suivre attentivement la syntaxe des commandes. Une erreur de syntaxe peut entraîner des problèmes lors de la création de la partition chiffrée.

5. **Chiffrement d'une Partition en Cours d'Utilisation :** Il est recommandé de chiffrer une partition lorsque le système de fichiers n'est pas en cours d'utilisation. Évitez de chiffrer une partition active pour éviter tout problème potentiel.


## Le chiffrement applicatif
Il consiste à ne chiffrer que les colonnes qui sont éligibles. Plus chirurgical, mais ce ne sera pas la solution adaptée s’il faut chiffrer toute la base. Dans ce cas, la colonne est stockée chiffrée sur disque, et ne pourra être déchiffrée qu’en fournissant la clé qui a permis l’encryption. Sans ce sésame, un fouillis de chiffres et lettres illisibles.
![[Pasted image 20231130222055.png]]
Parmi les inconvénients principaux, le manque de transparence vis-à-vis de l’application. Le code devra être modifié pour manipuler la ou les clés de chiffrement, ce qui exclue la solution pour nombre de progiciels qui ne l’ont pas prévu. L’impact sur la performance et la volumétrie est également très dissuasif, comme nous allons le voir plus loin.

### Exemple
```sql
CREATE TABLE T_CompteUtilisateur(
   IdCompteUtilisateur INT AUTO_INCREMENT,
   AddresseMail VARCHAR(8000),
   Nom VARCHAR(50),
   Prenom VARCHAR(50),
   NbrDeModification INT,
   NomUtilisateur VARCHAR(50),
   Mdp VARCHAR(255),
   PRIMARY KEY(IdCompteUtilisateur)
)ENGINE = INNODB DEFAULT CHARSET = latin1;

INSERT INTO `T_CompteUtilisateur` (`IdCompteUtilisateur`, `AddresseMail`, `Nom`, `Prenom`, `NbrDeModification`, `NomUtilisateur`, `Mdp`) VALUES
(15, 'email1@example.com', 'Nom1', 'Prenom1', 3, 'Utilisateur1', aes_encrypt('MotDePasse1', 'key')),
(4562, 'email2@example.com', 'Nom2', 'Prenom2', 5, 'Utilisateur2', aes_encrypt('MotDePasse2', 'key')),
(5554, 'email3@example.com', 'Nom3', 'Prenom3', 2, 'Utilisateur3', aes_encrypt('MotDePasse3', 'key'));
```

*source*: 
https://blog.capdata.fr/index.php/quelles-solutions-de-chiffrement-de-donnees-pour-mysql-mariadb/
https://www.youtube.com/watch?v=X7ACdLRb6Wk&t=4s
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
)ENGINE = INNODB DEFAULT CHARSET = latin1; -- bien préciser

INSERT INTO `T_CompteUtilisateur` (`IdCompteUtilisateur`, `AddresseMail`, `Nom`, `Prenom`, `NbrDeModification`, `NomUtilisateur`, `Mdp`) VALUES
(15, 'email1@example.com', 'Nom1', 'Prenom1', 3, 'Utilisateur1', aes_encrypt('MotDePasse1', 'key')),  -- bien garder la clé
(4562, 'email2@example.com', 'Nom2', 'Prenom2', 5, 'Utilisateur2', aes_encrypt('MotDePasse2', 'key')), -- bien garder la clé
(5554, 'email3@example.com', 'Nom3', 'Prenom3', 2, 'Utilisateur3', aes_encrypt('MotDePasse3', 'key')); -- bien garder la clé

SELECT *, cast(aes_decrypt(Mdp, 'key') as char(255)) from T_CompteUtilisateur

-- si possible créer une clé pour chaque utilisateur
```

*source*: https://www.youtube.com/watch?v=X7ACdLRb6Wk&t=4s
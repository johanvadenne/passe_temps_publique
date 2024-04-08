```sql
/* 
-- ATTENTION --
Si vous passez par l'API 
il faut au moin avoir la possibilité de lire la table 
si on veut pouvoir INSERT, UPDATE, DELETE.
Car l'API fait un 'show table' pour voir les tables avant de faire quoique se soit

pour une idée plus optimale et sécurisé je suis preneur
*/

CREATE USER 'johan'@'localhost' IDENTIFIED BY 'mdp';
CREATE USER 'maxime'@'localhost' IDENTIFIED BY 'mdp';
CREATE USER 'BugSafariAdmin'@'localhost' IDENTIFIED BY 'mdp';
CREATE USER 'BugSafariUtilisateur'@'localhost' IDENTIFIED BY 'mdp';

-- admin
GRANT ALL PRIVILEGES ON BugSafari_DEV.* TO 'johan'@'localhost';
GRANT ALL PRIVILEGES ON BugSafari_PROD.* TO 'johan'@'localhost';
GRANT ALL PRIVILEGES ON BugSafari_DEV.* TO 'maxime'@'localhost';
GRANT ALL PRIVILEGES ON BugSafari_PROD.* TO 'maxime'@'localhost';

-- BugSafariAdmin
GRANT SELECT ON BugSafari_DEV.T_Ticket TO 'BugSafariAdmin'@'localhost';
GRANT SELECT ON BugSafari_DEV.T_ModifBiome TO 'BugSafariAdmin'@'localhost';
GRANT SELECT ON BugSafari_DEV.T_ModifInsecte TO 'BugSafariAdmin'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON BugSafari_DEV.T_Insecte TO 'BugSafariAdmin'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON BugSafari_DEV.T_InsecteBiome TO 'BugSafariAdmin'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON BugSafari_DEV.T_Biome TO 'BugSafariAdmin'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON BugSafari_DEV.T_TypeInsecte TO 'BugSafariAdmin'@'localhost';
GRANT SELECT ON BugSafari_DEV.T_CompteUtilisateur TO 'BugSafariAdmin'@'localhost';
GRANT SELECT ON BugSafari_PROD.T_Ticket TO 'BugSafariAdmin'@'localhost';
GRANT SELECT ON BugSafari_PROD.T_ModifBiome TO 'BugSafariAdmin'@'localhost';
GRANT SELECT ON BugSafari_PROD.T_ModifInsecte TO 'BugSafariAdmin'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON BugSafari_PROD.T_Insecte TO 'BugSafariAdmin'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON BugSafari_PROD.T_InsecteBiome TO 'BugSafariAdmin'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON BugSafari_PROD.T_Biome TO 'BugSafariAdmin'@'localhost';
GRANT SELECT, INSERT, UPDATE, DELETE ON BugSafari_PROD.T_TypeInsecte TO 'BugSafariAdmin'@'localhost';
GRANT SELECT ON BugSafari_PROD.T_CompteUtilisateur TO 'BugSafariAdmin'@'localhost';

-- BugSafariUtilisateur
GRANT SELECT ON BugSafari_DEV.T_TypeInsecte TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT ON BugSafari_DEV.T_Insecte TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT, INSERT, DELETE ON BugSafari_DEV.T_Favorie TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT ON BugSafari_DEV.T_InsecteBiome TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT ON BugSafari_DEV.T_Biome TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT, INSERT ON BugSafari_DEV.T_CompteUtilisateur TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT, INSERT ON BugSafari_DEV.T_ModifInsecte TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT, INSERT ON BugSafari_DEV.T_ModifBiome TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT ON BugSafari_PROD.T_TypeInsecte TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT ON BugSafari_PROD.T_Insecte TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT, INSERT, DELETE ON BugSafari_PROD.T_Favorie TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT ON BugSafari_PROD.T_InsecteBiome TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT ON BugSafari_PROD.T_Biome TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT, INSERT ON BugSafari_PROD.T_CompteUtilisateur TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT, INSERT ON BugSafari_PROD.T_ModifInsecte TO 'BugSafariUtilisateur'@'localhost';
GRANT SELECT, INSERT ON BugSafari_PROD.T_ModifBiome TO 'BugSafariUtilisateur'@'localhost';
-- aucune modification (UPDATE) n'est nécéssaire pour un utilisateur

FLUSH PRIVILEGES;
```
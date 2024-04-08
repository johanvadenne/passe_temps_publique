CREATE TABLE T_Biome(
   IdBiome INT AUTO_INCREMENT,
   Temperature DECIMAL(15,2),
   Nom VARCHAR(50),
   TauxHumidite DECIMAL(15,2),
   Descrition VARCHAR(8000),
   Environement VARCHAR(50),
   PRIMARY KEY(IdBiome)
);

CREATE TABLE T_CompteUtilisateur(
   IdCompteUtilisateur INT AUTO_INCREMENT,
   AddresseMail VARCHAR(8000),
   Nom VARCHAR(50),
   Prenom VARCHAR(50),
   NbrDeModification INT,
   NomUtilisateur VARCHAR(50),
   Mdp VARCHAR(255),
   PRIMARY KEY(IdCompteUtilisateur)
);

CREATE TABLE T_TypeInsecte(
   IdTypeInsecte INT AUTO_INCREMENT,
   Nom VARCHAR(50),
   Description VARCHAR(8000),
   PRIMARY KEY(IdTypeInsecte)
);

CREATE TABLE T_Ticket(
   IdTicket INT AUTO_INCREMENT,
   IdCompteUtilisateur INT NOT NULL,
   PRIMARY KEY(IdTicket),
   FOREIGN KEY(IdCompteUtilisateur) REFERENCES T_CompteUtilisateur(IdCompteUtilisateur)
);

CREATE TABLE T_ModifBiome(
   IdModifBiome INT AUTO_INCREMENT,
   Nom VARCHAR(50),
   Temperature DECIMAL(15,2),
   TauxHumidite DECIMAL(15,2),
   Descrition VARCHAR(8000),
   Environement VARCHAR(50),
   IdBiome INT NOT NULL,
   IdTicket INT NOT NULL,
   PRIMARY KEY(IdModifBiome),
   UNIQUE(IdTicket),
   FOREIGN KEY(IdBiome) REFERENCES T_Biome(IdBiome),
   FOREIGN KEY(IdTicket) REFERENCES T_Ticket(IdTicket)
);


CREATE TABLE T_ModifInsecte(
   IdInsecteModif INT AUTO_INCREMENT,
   Nom VARCHAR(50),
   Description VARCHAR(8000),
   Poids DECIMAL(15,2),
   UniteMasse VARCHAR(50),
   Taille DECIMAL(15,2),
   UniteTaille VARCHAR(50),
   Menace SMALLINT,
   Dangereusite VARCHAR(50),
   Saison VARCHAR(50),
   longevite DECIMAL(15,2),
   IdInsecte INT NOT NULL,
   IdTicket INT NOT NULL,
   PRIMARY KEY(IdInsecteModif),
   UNIQUE(IdTicket),
   FOREIGN KEY(IdInsecte) REFERENCES T_Insecte(IdInsecte),
   FOREIGN KEY(IdTicket) REFERENCES T_Ticket(IdTicket)
);

CREATE TABLE T_Insecte(
   IdInsecte INT AUTO_INCREMENT,
   Nom VARCHAR(50),
   Description VARCHAR(8000),
   Poids DECIMAL(15,2),
   UniteMasse VARCHAR(50),
   Taille DECIMAL(15,2),
   UniteTaille VARCHAR(50),
   Menace SMALLINT,
   Dangereusite VARCHAR(50),
   Saison VARCHAR(50),
   longevite DECIMAL(15,2),
   IdTypeInsecte INT NOT NULL,
   PRIMARY KEY(IdInsecte),
   FOREIGN KEY(IdTypeInsecte) REFERENCES T_TypeInsecte(IdTypeInsecte)
);

CREATE TABLE T_Favorie(
   IdFavorie INT AUTO_INCREMENT,
   IdCompteUtilisateur INT NOT NULL,
   IdInsecte INT NOT NULL,
   PRIMARY KEY(IdFavorie),
   FOREIGN KEY(IdCompteUtilisateur) REFERENCES T_CompteUtilisateur(IdCompteUtilisateur),
   FOREIGN KEY(IdInsecte) REFERENCES T_Insecte(IdInsecte)
);

CREATE TABLE T_MiseAJour(
   IdMiseAJour INT AUTO_INCREMENT,
   DateModif DATETIME,
   IdCompteUtilisateur INT NOT NULL,
   IdBiome INT NOT NULL,
   IdInsecte INT NOT NULL,
   PRIMARY KEY(IdMiseAJour),
   FOREIGN KEY(IdCompteUtilisateur) REFERENCES T_CompteUtilisateur(IdCompteUtilisateur),
   FOREIGN KEY(IdBiome) REFERENCES T_Biome(IdBiome),
   FOREIGN KEY(IdInsecte) REFERENCES T_Insecte(IdInsecte)
);

CREATE TABLE T_InsecteBiome(
   IdInsecteBiome INT AUTO_INCREMENT,
   IdBiome INT NOT NULL,
   IdInsecte INT NOT NULL,
   PRIMARY KEY(IdInsecteBiome),
   FOREIGN KEY(IdBiome) REFERENCES T_Biome(IdBiome),
   FOREIGN KEY(IdInsecte) REFERENCES T_Insecte(IdInsecte)
);

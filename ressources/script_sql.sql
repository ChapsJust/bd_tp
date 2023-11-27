DROP DATABASE IF EXISTS bd_tp;
CREATE DATABASE bd_tp;
USE bd_tp;

CREATE TABLE Utilisateur(
id_utilisateur INTEGER AUTO_INCREMENT PRIMARY KEY,
nom VARCHAR(255),
droits VARCHAR(255)
);

CREATE TABLE Livre(
id_livre INTEGER AUTO_INCREMENT PRIMARY KEY,
titre VARCHAR(255),
auteur VARCHAR(255)
);

CREATE TABLE chapitre(
id_chapitre INTEGER AUTO_INCREMENT PRIMARY KEY,
id_livre INTEGER,
no_chapitre VARCHAR(255),
texte text,
FOREIGN KEY(id_livre) REFERENCES Livre(id_livre)
);

CREATE TABLE Personnage(
id_personnage INTEGER AUTO_INCREMENT PRIMARY KEY,
id_sauvgarde INTEGER,
id_fiche INTEGER,
nom VARCHAR(255),
disiplines VARCHAR(255),
armes VARCHAR(255),
objets VARCHAR(255),
repas VARCHAR(255),
objets_speciaux VARCHAR(255),
bourse INTEGER
);

CREATE TABLE lien_chapitre(
id_lien_chapitre INTEGER AUTO_INCREMENT PRIMARY KEY,
no_chapitre_origine INTEGER,
no_chapitre_destination INTEGER
);

CREATE TABLE Sauvegarde(
  id_sauvegarde INTEGER AUTO_INCREMENT PRIMARY KEY,
  id_utilisateur INTEGER,
  id_chapitre INTEGER,
  id_personnage INTEGER,
  nom_sauvegarde VARCHAR(255)
);

CREATE USER IF NOT EXISTS 'player' IDENTIFIED BY 'qwerty';

GRANT SELECT, INSERT, UPDATE, DELETE ON bd_tp.* TO 'player';


DELIMITER $$
CREATE TRIGGER perso ON AFTER INSERT ON Personnage FOR EACH ROW
BEGIN 
    DECLARE message VARCHAR(255);
    SET message = 'Insert into Personnage table reussie';
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = message;
END

CREATE TRIGGER usager ON AFTER INSERT ON Utilisateur FOR EACH ROW
BEGIN 
    DECLARE message VARCHAR(255);
    SET message = 'Insert into utilisateur table reussie';
    SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = message;
END
DELIMITER ;















ahier des charges BugSafari - Version [Insérer la version ici]
Date de révision : [Insérer la date ici]

Présentation :

Il s'agit d'un projet de niveau BTS, réalisé par deux étudiants, visant à développer une application mobile destinée aux utilisateurs, ainsi qu'une interface web dédiée aux administrateurs pour superviser les créations et modifications des utilisateurs.


1. Introduction

BugSafari est une application Android conçue pour les amateurs d'entomologie, les chercheurs et les curieux de la faune qui souhaitent explorer le monde fascinant des insectes. Cette application permet aux utilisateurs de découvrir et de comprendre la diversité incroyable des insectes qui peuplent notre planète, en utilisant une variété de critères de recherche pour personnaliser leur exploration, ils auront la possibilité de consulter une fiche technique détaillée sur les insectes pour explorer en profondeur leurs caractéristiques.

2. Plateforme

BugSafari sera développé pour la plateforme Android, afin de suivre les tendances actuelles du marché et d'attirer un large public.

3. Description du Projet

3.1 Description Approfondie

L'application BugSafari se compose des principales fonctionnalités suivantes :

3.1.1 Accueil
- L'accueil est la première page accessible depuis l'ouverture de l'application ou en cliquant sur le logo.
- Présentation sommaire de l'application.
- Possibilité de connexion pour les utilisateurs enregistrés.

3.1.2 Recherche
- Permet aux utilisateurs de rechercher des insectes en utilisant une barre de recherche.
- Possibilité de trier et de filtrer les résultats en fonction de critères tels que le nom, la taille, le type, le biome, le niveau de danger, etc.

3.1.3 Biome
- Affiche une fiche technique détaillée pour chaque biome, comprenant des informations telles que le taux d'humidité et d'autres caractéristiques.
- Possibilité de rechercher les insectes spécifiques à un biome donné.

3.1.4 Nouveautés
- Affiche les derniers insectes modifiés ou ajoutés à la base de données.

3.1.5 Fonctionnalités pour les utilisateurs connectés
- Possibilité de mettre en favori des insectes.
- Possibilité d'ajouter ou de modifier des informations sur des insectes (soumis à validation par les administrateurs).
- Certification des utilisateurs par les administrateurs après un certain nombre de modifications validées.

3.2 Web (Ticketing)

Les utilisateurs connectés peuvent soumettre des demandes de modification ou d'ajout de fiches techniques concernant un biome ou un insecte. Ces demandes seront traitées sous forme de tickets par les administrateurs.

4. Outils Utilisés

- GitHub : Gestion du projet
- Android Studio : Logiciel de développement
- Langage : C#
- Obsidian : Documentation
- Visual Studio Code : UML
- NGINX : API
- SQL Server ou MariaDB : Base de données
- Hébergement : À déterminer
- Looping : Structure de la base de données

5. Nomenclature

- Nommage de table : T_NomDeLaColonne
- Variables et procédures : Singulier, verbe à l'infinitif, nommage en CamelCase (ex : maVariable)
- Tableaux : Commencent par "tab"

6. Structure de la Base de Données

Voici la structure de la base de données avec les principales tables :

- T_Biome
- T_CompteUtilisateur
- T_TypeInsecte
- T_Insecte
- T_Favori
- T_MiseAJour
- T_InsecteBiome

7. Vocabulaire

Pour garantir une cohérence dans le vocabulaire utilisé dans l'application, nous adopterons les termes suivants :
- Biome : Désigne un écosystème spécifique.
- Insecte : Désigne un insecte spécifique.
- Favori : Désigne les insectes marqués comme favoris par les utilisateurs.
- Mise à Jour : Désigne les modifications apportées aux informations sur les insectes et aux biomes.

8. Conclusion

Ce cahier des charges définit les principales fonctionnalités, les outils utilisés et la structure de la base de données pour l'application BugSafari. L'équipe de développement est chargée de mettre en œuvre ces spécifications pour créer une application Android robuste et conviviale pour les amateurs d'entomologie et les passionnés de la faune.
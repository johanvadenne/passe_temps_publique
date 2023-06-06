<?php

#je demande combien d'utilisateur veut-il enregistrer
echo("combien il y a d'utilisateur voulez-vous enregistrer\n");

#j'enregistre la valeur
$nombre_utilisateur = readline();

#je créer une boucle jusqu'à se que le dernier utilisateur soit crée
for ($i=0; $i < $nombre_utilisateur; $i++) {

#je demande d'entré le nom de l'utilisateur
    echo("entré le nom de l'utilisateur\n");

#j'enregistre la valeur
    $utilisateurs[$i] = readline();
}

#j'écris 2 utilisateur au hasard
echo("voici 2 utilisateurs au hasard\n");

#je choisi un utilisateur au hasard
$utilisateurs_hasard = rand(0, $nombre_utilisateur);
echo("$utilisateurs[$utilisateurs_hasard]\n");

#je choisi un utilisateur au hasard
$utilisateurs_hasard = rand(0, $nombre_utilisateur);
echo("$utilisateurs[$utilisateurs_hasard]\n");
<?php

#saisissé un chiffre
echo("saisissé un nombre\n");

#j'enregistre le chiffre
$chiffre = readline();

#je définie le nombre de fois que mla boucle va tourner
$boucle = strlen($chiffre);

#créer une variable
$resulat = 0;

#boucle
for ($i=0; $i < $boucle; $i++) { 
    $tableau = $boucle - 1;
    $resulat = $resulat + $chiffre[$tableau];
}

#je dis le chiffre à l'envers
echo("$resulat\n");
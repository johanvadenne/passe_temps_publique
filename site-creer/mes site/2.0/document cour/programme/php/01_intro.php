<?php
//02_intro.php

// je me présente
$name = "Vadenne ";
$prenom = "Johan ";
$age = 17;
echo "\nMon nom est ". $name;
echo "\net mon prénom ". $prenom;
echo "\nj'ai actuelement ". $age." ans.";

//-------------------------------------------------------------------------------------

//je te demande de te presenter
echo "\nqu'elle est ton nom de famille : ";
$tonnom = fgets(STDIN);
echo "\nqu'elle est ton prenom : ";
$tonprenom = fgets(STDIN);
echo "\nqu'elle est ton age : ";
$tonage = fgets(STDIN);
echo "\ntu t'appelle ".$tonnom. $tonprenom ."tu as" .$tonage." ans.\n";

//si sinon
if ($tonage > 60) {
    echo "\ntu est vieux";
} 
elseif ($tonage > 60) {
    echo "\ntu commence a te faire vieux";
}
else {
    echo "\ntu est encore jeune";
}

//-------------------------------------------------------------------------------------

//petit je de calcul
echo "\nchoisie un nombre : ";
$nombre1 = fgets(STDIN);
echo "\nchoisie un deuxieme nombre : ";
$nombre2 = fgets(STDIN);
$resultat = $nombre1 * $nombre2;
echo "\nle resultat de la multiplication ". $resultat;


//pour lancer le programme --> php .\01_intro.php
<?php
#création de la constante ANNEE
define('ANNEE', 2022);

# je demande l'age, le nom et le prenom
echo "qu'elle est ton âge?:\n";
$age = trim(fgets(STDIN));
echo "qu'elle est ton nom?:\n";
$nom = trim(fgets(STDIN));
echo "qu'elle est ton prénom?:\n";
$prenom = trim(fgets(STDIN));

# calcule de l'annee de naissance
$naissance = ANNEE - $age;

# je le salut
echo "Bonjour $prenom ". strtoupper("$nom.\n");

# je dit son annee de naissance
echo "Vous est née en $naissance.\n";

# creation de la variable bougie
$bougie = "";

#boucle for pour ajouter autant de bougie que son age
for ($i=0; $i < $age; $i++) { 
    $bougie = $bougie. "🕯️";
}
echo $bougie;


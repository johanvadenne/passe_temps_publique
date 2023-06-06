<?php
echo "\nqu'elle est ton age : ";
$tonage = fgets(STDIN);

//si sinon
if ($tonage > 60) {
    echo "\ntu est vieux";
} 
elseif ($tonage > 50) {
    echo "\ntu commence a te faire vieux";
} 
elseif ($tonage > 40) {
    echo "\ntu n'est plus tout jeune";
}
else {
    echo "\ntu est encore jeune";
}

//-------------------------------------------------------------------------------------

//boucle ajoute 1 tant que i < 10
for ($i=0; $i < 10; $i++) { 
    echo "\n". $i;
}

//-------------------------------------------------------------------------------------

//vérification de mot de passe : attention mettre trim(fgets(STDIN));

echo "\nmot de passe : boite\n";
$motdepasse = trim(fgets(STDIN));
echo strlen($motdepasse). "\n";

if ($motdepasse == "boite") {
    echo "Bienvenue chez vous";
}
else {
    echo "\nERREUR :\n mot de passe incorrect";
}

echo "\nmot de passe : 1234\n";
$motdepasse = trim(fgets(STDIN));
echo strlen($motdepasse). "\n";

if ($motdepasse == 1234) {
    echo "Bienvenue chez vous";
}
else {
    echo "\nERREUR :\n mot de passe incorrect";
};
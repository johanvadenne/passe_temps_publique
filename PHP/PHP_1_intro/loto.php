<?php
#je définie un nombre de crédit
define("CREDIT", 100);

#je défini une variable qui définit le nombre de crédit et un nombre aléotoire entre 1 et 3
$credit = CREDIT;
$loto = rand(1, 3);

#je créer une boucle qui continura tant que j'ai des crédiit
while($credit >= 0){

#je demande le nombre de crédit mis en jeu
    echo"Combien voulez vous misé de crédit?\n Vous avez $credit crédit(s):\n";
    $mise = trim(fgets(STDIN));

#je demande qu'elle est le chiffre gagnant
    echo"Qu'elle est le chiffre gagnant: 1 ou 3\n";
    $chiffre = trim(fgets(STDIN));

#je reinitialise mon chiffre du loto
    $loto = rand(1, 3);

#si il a trouvé le bon numéro
    if($chiffre == $loto){

#il gagne le double de sa mise
        $credit = $credit + $mise;
        echo"BRAVO!!! vous avez gagnez\n";
    }

#si il n'a pas trouvé le numéro
    else
    {

#il perd sa mise
        $credit = $credit - $mise;
        echo"PERDU!!!\n";
        echo"le chiffre était $loto\n";
    }
}
echo"vous n'avez plus de crédit au revoir!\n";
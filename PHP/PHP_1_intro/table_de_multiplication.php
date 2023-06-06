<?php
/* je définie le nombre de table de multiplication que je veux */
define("TABLE", 10);

/* je définie 3 variable : le nombre de la table définie/ le nombre multiplicateur/ $i pour la boucle */
$table = 0;
$multi = 0;
$i = 0;

/* boucle qui créer les tables de multiplications */
for ($i = 0; $i < TABLE; $i++){

    /* je définie la table de multiplication */
    $table++;
    echo"Table de $table\n";

    /* je reinitialise le multiplicateur */
    $multi = 0;

    /* j'ecris la table de multiplication */
    while($multi < TABLE){
    $c = $table * $multi;
    echo"$table x $multi = $c\n";
    $multi++;
    }
}
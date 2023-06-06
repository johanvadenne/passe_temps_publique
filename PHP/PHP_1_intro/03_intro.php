<?php
//boucle : while
$a = 0;
$b = "\n";
//boucle qui ajoute 1 tant que $a est inférieure à 10
while ($a < 100000000) {
    echo $a. $b;
    $a = $a + 1;
    if ($a == 99999999){
        $a = $a - 9999999999;
    }
}
echo $a. "\n";

//-------------------------------------------------------------------------------------

//demande un nombre entre 1 et 100
$n = -1;
while ($n < 0 || $n > 100){
    echo "choisi un nombre entre 0 et 100:\n";
    $n = trim(fgets(STDIN));
}

$r = 100 - $n;
$c = "; ";

//boucle qui ajoute 1 tant que $n est inférieure à 100
while ($n < 100) {
    echo $n. $c;
    $n++;
}
echo $n. $c. "\n";
echo "j'ai rajouté ". $r. " pour arriver à 100.\n";


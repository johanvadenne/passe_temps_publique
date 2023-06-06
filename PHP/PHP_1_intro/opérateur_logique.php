<?php
//opérateur logique || && ^ !
$a = -1;
$b = -1;

while ($a < 0 || $a > 10  || $b < 0 || $b > 10) {
    
    echo "donne moi un nombre en 0 et 10\n";
    $a = trim(fgets(STDIN));
    echo "donne moi le même nombre en 0 et 10\n";
    $b = trim(fgets(STDIN));
    echo "désolé mais tu as choisie un chiffre au dessus 10 ou en dessous de 0\n";
}
if ($a == $b){
    echo $a, " est bien égale ", $b;
}
else {
    echo $a, " n'est pas égale ", $b;
}
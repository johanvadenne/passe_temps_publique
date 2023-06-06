<?php
$a = "";
for ($i=0; $i < 10; $i++) { 
    echo $a. "\n";
    $a = $a. "*";
}

$c = "";
echo "donne moi un nombre\n";
$b = trim(fgets(STDIN));
for ($i=0; $i < $b; $i++) { 
    $c = $c. "*";
}
echo $c;
<?php

define("NOMBRE", 100);
$nombre = NOMBRE;
while ($nombre != 0){
    echo"$nombre\n";
    $nombre--;
}
echo"$nombre\n";

define("NOMBRE2", 100);
$i = NOMBRE2;
for ($i = NOMBRE2; $i >= 0; $i--){
    echo"$i\n";
}
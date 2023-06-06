<?php

// On définie une cible
$host = 'google.com';

// On définie les ports que l'on veut scanner
$ports = array(21, 25, 80, 81, 110, 143, 443, 587, 2525, 3306);

// On parcours tout les port du tableau
foreach ($ports as $port)
{
    // Cette fonction va se connecté à "$host" via le port parcouru du tableau
    $connection = @fsockopen($host, $port, $errno, $errstr, 2);

    // Si la connection via se port est réussi alors:
    if (is_resource($connection))
    {
        // Affichage du numéro et le nom du port
        // Getservbyport renvoie le nom du port
        echo $host . ': ' . $port . ' ' . getservbyport($port, 'tcp') . " is open\n";

        // On arrête la connection 
        fclose($connection);
    }
    else
    {
        echo $host . ': ' . $port . getservbyport($port, ' tcp') . " is not open\n";
    }
}
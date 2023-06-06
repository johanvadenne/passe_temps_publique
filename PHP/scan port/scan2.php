<?php

// On définie une cible
echo "Nom host: ";
$host = readline();

// scan de tout les ports
for ($i=0; $i < 65536; $i++) {

    // Cette fonction va se connecté à "$host" via le port parcouru du tableau
    $connection = @fsockopen($host, $i, $errno, $errstr, 2);
    // Si la connection via se port est réussi alors:
    if (is_resource($connection))
    {
        // Affichage du numéro et le nom du port
        // Getservbyport() renvoie le nom du port
        echo $host . ': ' . $i . ' ' . getservbyport($i, 'tcp') . " is open\n";

        // On arrête la connection 
        fclose($connection);
    }
    else
    {
        echo $host . ': ' . $i . " " . getservbyport($i, 'tcp') . " is not open\n";
    }
}
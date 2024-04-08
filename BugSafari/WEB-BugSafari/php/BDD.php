<?php
require 'php/lien_BDD.php';


// Exécuter des requêtes SQL et renvoyer les résultats au format JSON
$result = $conn->query("SELECT * FROM T_Ticket");
$data = array();

while ($row = $result->fetch_assoc()) {
    $data[] = $row;
}

echo json_encode($data);

// Fermer la connexion
$conn->close();
?>

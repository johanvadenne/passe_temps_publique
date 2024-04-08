<?php
$servername = "localhost";
$username = "maxime";
$password = "CamilleLaChenille";
$database = "BugSafari_DEV";

// Créer une connexion
$conn = new mysqli($servername, $username, $password, $database);

// Vérifier la connexion
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}


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

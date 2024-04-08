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

// Récupérer l'ID à partir de la requête GET
$id = $_GET['id'];

echo $id;

// Exécuter la requête de suppression
$result = $conn->query("DELETE FROM T_Ticket WHERE IdTicket = 2");

echo "réussie";

// Fermer la connexion
$conn->close();
?>

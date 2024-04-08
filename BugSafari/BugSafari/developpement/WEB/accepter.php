<?php
// Connexion à la base de données (à adapter selon votre configuration)
$servername = "localhost";
$username = "maxime";
$password = "CamilleLaChenille";
$database = "BugSafari_DEV";

$conn = new mysqli($servername, $username, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Récupérer l'ID à partir de la requête GET
$id = $_GET['id'];

// Exécuter la requête de suppression
$sql = "DELETE FROM T_Ticket WHERE IdTicket = $id";

if ($conn->query($sql) === TRUE) {
    echo json_encode(['success' => true, 'message' => 'Changement accepté avec succès.']);
} else {
    echo json_encode(['success' => false, 'message' => 'Erreur lors de l\'acceptation du changement: ' . $conn->error]);
}

// Fermer la connexion
$conn->close();
?>

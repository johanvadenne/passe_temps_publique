<?php
require 'php/lien_BDD.php';

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

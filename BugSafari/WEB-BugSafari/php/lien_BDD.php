<?php

require __DIR__ . '/vendor/autoload.php';

$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$typeBDD=$_ENV['TYPEBDD'];
$host=$_ENV['HOST'];
$dbname=$_ENV['BDDNAME'];
$username=$_ENV['USERNAME'];
$password=$_ENV['PASSWORD'];

try {
    // Créer une connexion PDO
    $bdd = new PDO("$typeBDD:host=$host;dbname=$dbname", $username, $password);
    // Définir le mode d'erreur sur Exception
    $bdd->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    die("Connection failed: " . $e->getMessage());
}
?>
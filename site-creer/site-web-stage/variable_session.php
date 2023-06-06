<?php

session_start();

$_SESSION["utilisateur"] = "21232f297a57a5a743894a0e4a801fc3";
$_SESSION["Mdp"] = "21232f297a57a5a743894a0e4a801fc3";

if (isset($_POST["connexion"])) {
    if (md5($_POST["utilisateur"]) == $_SESSION["utilisateur"] && md5($_POST["Mdp"]) == $_SESSION["Mdp"]) {
        header("location:page_eleve.php");
    }
}


?>

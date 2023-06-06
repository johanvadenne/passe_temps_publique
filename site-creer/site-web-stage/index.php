<?php include("variable_session.php"); ?>

<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Stage</title>
</head>

<body>
    
    <!-- fond écran -->
    <div class="fond">
        <img src="image/logo_FDN.png">
    </div>

    <div class="authentification">
        <form method="post">
            <input class="saisie" type="text" name="utilisateur" placeholder="utilisateur"><br><br>
            <input class="saisie" type="password" name="Mdp" placeholder="Mot de passe"><br><br>
            <input type="submit" class="connexion" name="connexion" value="Se connecter">
        </form>
    </div>

</body>

</html>

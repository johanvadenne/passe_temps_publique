<?php
require 'php/lien_BDD.php';
if(isset($_POST['envoi'])){
  if(!empty($_POST['pseudo']) AND !empty($_POST['mdp'])){
    $pseudo = ($_POST['pseudo']);
    $mdp = sha1($_POST['mdp']);

    $recupUser = $bdd->prepare('SELECT * FROM T_CompteUtilisateur WHERE Nom = ? AND Mdp = ?');
    $recupUser->execute(array($pseudo, $mdp));

    if($recupUser->rowCount()>0){
      header('location: index.html');
      
    }else{
      echo "Erreur";
    }

  }else{
    echo "Veuillez compléter tout les champs...";
  }
  
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="css/login.css?v=2" rel="stylesheet">
    <title>Document</title>
</head>
<body>
    
    <div class="login-box">
        <h2>Login</h2>
        <form method="POST" action="" autocomplete="off">
          <div class="user-box">
            <input type="text" name="pseudo" required="">
            <label>Nom</label>
          </div>
          <div class="user-box">
            <input type="password" name="mdp" required="">
            <label>Mot de passe</label>
          </div>
          <button type="submit" name="envoi">
            <span></span>
            <span></span>
            <span></span>
            <span></span>
            Envoyer
          </button>
          </a>
        </form>
      </div>
</body>
</html>
## sha1
```sql

$pseudo = ($_POST['pseudo']);
$mdp = sha1($_POST['mdp']);

$recupUser = $bdd->prepare('SELECT * FROM T_CompteUtilisateur WHERE Nom = ? AND Mdp = ?');
$recupUser->execute(array($pseudo, $mdp));
```
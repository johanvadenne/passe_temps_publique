<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous">
    <title>Satge</title>
</head>

<body>

    <!-- fond écran -->
    <div class="fond">
        <img src="image/logo_FDN.png">
    </div>

    <!-- onglet: Entreprise | Élève -->
    <div class="onglet">
        <a href="page_entreprise.php">Entreprise</a>
        <a href="page_eleve.php">Élève</a>
    </div>

    <!-- titre -->
    <span class="titre"><h1>Entreprise</h1></span>

    <!-- nom utilisateur -->
    <div class="utilisateur">
        <h3>Nicola</h3>
        <h4>Cosneau</h4>
    </div>

    <!-- bouton: ajouter |  modifier | supprimer -->
    <div class="bouton">
        <input type="button" value="ajouter" onclick="window.location.href = 'ajouter_entreprise.html'">
        <input type="button" value="modifier" onclick="window.location.href = 'modifier_entreprise.html'">
        <input type="button" value="supprimer" onclick="window.location.href = 'supprimer_entreprise.html'">
    </div>

    <!-- tableau des entreprises générer automatiquement -->
    <div class="table_entreprise">
        <table>
            <tr>
                <th>Nom de l'entreprise</th>
                <th>Site web</th>
                <th>Adresse</th>
                <th>Ville</th>
                <th>Adresse mail</th>
                <th>Nbr de stagiaires déjà pris</th>
                <th>Ressenti des élèves</th>
                <th>Nbr de stagiaires pris</th>
            </tr>
            <?php require("entreprise.php"); ?>
        </table>
    </div>

    <!-- lien site: Lycéé Fénélon Notre Dame -->
    <footer>
        <a href="https://fenelon-notredame.com/"><b>Lycéé Fénélon Notre Dame</b></a>
    </footer>
</body>

</html>
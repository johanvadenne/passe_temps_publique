<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" type="text/css" href="style.css" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-aFq/bzH65dt+w6FI2ooMVUpc+21e0SRygnTpmBvdBgSdnuTN7QbdgL+OapgHtvPp" crossorigin="anonymous" />
    <title>Stage</title>
</head>

<body>

    <!-- fond écran -->
    <div class="fond">
        <img src="image/logo_FDN.png" />
    </div>

    <!-- onglet: Entreprise | Élève -->
    <div class="onglet">
        <a href="page_entreprise.php">Entreprise</a>
        <a href="page_eleve.php">Élève</a>
    </div>

    <!-- titre -->
    <span class="titre">
        <h1>Élève</h1>
    </span>

    <!-- nom utilisateur -->
    <div class="utilisateur">
        <h3>Nicola</h3>
        <h4>Cosneau</h4>
    </div>

    <!-- bouton: ajouter |  modifier | supprimer -->
    <div class="bouton">
        <input type="button" value="ajouter" onclick="window.location.href = 'ajouter_eleve.html'" />
        <input type="button" value="modifier" onclick="window.location.href = 'modifier_eleve.html'" />
        <input type="button" value="supprimer" onclick="window.location.href = 'supprimer_eleve.html'" />
    </div>

    <!-- tableau des élèves générer automatiquement -->
    <div class="table_eleve">
        <table>
            <?php
            require(".base_de_donnee.php");
            $db = new DB;
            $db->connexion();
            $db->affiche("etudiant");
            ?>
        </table>
    </div>

    <!-- lien site: Lycéé Fénélon Notre Dame -->
    <footer>
        <a href="https://fenelon-notredame.com/"><b>Lycéé Fénélon Notre Dame</b></a>
    </footer>
</body>

</html>
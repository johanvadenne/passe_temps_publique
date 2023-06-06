<?php

class Etudiant {
    private $id_eleve;
    private $nom;
    private $prenom;
    private $age;
    private $scolarite;
    private $id_entreprise;
}

class Entreprise {
    
    private $id_eleve;
    private $nom;
    private $site_web;
    private $adresse;
    private $ville;
    private $mail;
    private $Nbr_stagiaires_deja_pris;
    private $ressenti_des_eleves;
    private $Nbr_stagiaires_pris;
}

class DB {

    // utilisateur: A CHANGER!!!
    private $db_user = "utilisateur";
    // mot de passe: A CHANGER!!!
    private $db_password = "mot de passe";
    // nom de la base de donnée
    private $db_name = "courb1_nc";
    // dsn: data source name
    private $dsn = "mysql:host=localhost;dbname=";
    // dsn: data source name
    private $data_base;

    public function connexion() {

        // configuration du dsn
        $this->dsn .= $this->db_name;

        // connection à la base de donnée
        $this->data_base = new PDO($this->dsn, $this->db_user, $this->db_password);

        // test si de connection
        $connect = $this->data_base->query("SHOW TABLES;");

        // si connection échoué: arrêter!
        if ($connect == false) {
            die("connection à la base de donnée échoué");
        }
    }


    public function affiche(string $nom_table, int $id = 0) {

        // initialization variable
        $reqSQL = "";
        $tableHTML = "";
        $titre_creer =false;

        // créer la requête
        $reqSQL = "SELECT * FROM $nom_table $condition";

        // parcours le résultat
        $resultat = $this->data_base->query($reqSQL, PDO::FETCH_ASSOC);
        foreach($resultat as $ligne) {

            if (!$titre_creer) {

                // ouvre une ligne
                $tableHTML .= "<tr>\n";

                // remplie la ligne
                foreach($ligne as $colonne) {
                    $tableHTML .= "<th>$colonne</th>\n";
                }
                
                // ferme la ligne
                $tableHTML .= "</tr>\n";

                $titre_creer = true;
            }

            $tableHTML .= "<th>action</th>\n";

            // ouvre une ligne
            $tableHTML .= "<tr>\n";

            // remplie la ligne
            foreach($ligne as $colonne) {
                $tableHTML .= "<td>$colonne</td>\n";
            }
            
            $tableHTML .= '<td><a href="modifier_eleve>🖊</a><a href="supprimer_eleve>❌</a></td>\n';

            // ferme la ligne
            $tableHTML .= "</tr>\n";
        }

        echo $tableHTML;
    }
}

?>

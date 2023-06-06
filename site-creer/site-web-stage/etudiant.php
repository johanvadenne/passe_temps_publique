<?php
class Etudiant {
    private $id;
    private $nom;
    private $prenom;
}

class DB {
    public function connexion() {
        $data_base = new PDO('mysql:host=localhost;dbname=courb1_nc', 'utilisateur', 'mdp');

            foreach($data_base->query('SELECT * from etudiant') as $row) {
                echo "
                <tr>\n
                    <td>$row[1]</td>\n
                    <td>$row[2]</td>\n
                    <td>$row[3]</td>\n
                    <td>$row[4]</td>\n
                    <td>$row[5]</td>\n
                </tr>\n
                ";
            }
    }
}

$db = new DB();
$db->connexion();
?>

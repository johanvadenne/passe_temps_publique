<?php
class entreprise {
    private $id;
    private $nom;
}

class DB {
    public function connexion() {
        $data_base = new PDO('mysql:host=localhost;dbname=courb1_nc', 'utilisateur', 'mdp');

            foreach($data_base->query('SELECT * from entreprise') as $row) {
                echo "
                <tr>\n
                    <td>$row[1]</td>\n
                    <td>$row[2]</td>\n
                    <td>$row[3]</td>\n
                    <td>$row[4]</td>\n
                    <td>$row[5]</td>\n
                    <td>$row[6]</td>\n
                    <td>$row[7]</td>\n
                    <td>$row[8]</td>\n
                </tr>\n
                ";
            }
    }
}

$db = new DB();
$db->connexion();
?>

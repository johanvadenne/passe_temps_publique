<?php

class BDD {

    // init
    private PDO $pdo;
    private string $dsn;
    private string $typeBDD;
    private string $host;
    private string $dbname;
    private string $username;
    private string $password;
    private array $tabTable;
    private array $tabErreur = ["ERREUR" => ""];

    /*
    FR:
        - informations de connexion à la base de données
        - connexion à la base de données
        - répertorie les tables de la base de données
    EN: database connection
        - database connection information
        - database connection
        - lists database tables
    */
    function __construct() {
        $this->typeBDD="";
        $this->host="";
        $this->dbname="";
        $this->username="";
        $this->password='';
        // $this->username="BugSafariUtilisateur";
        // $this->password='YqZpd$U!39&Lv6oxU@YoV!T*A&Hui%Hn5@ocowKp23hSJ&39x3oaa%K&YAXJJ&Uk22*4PK^&gY&yo5PXf!@sckRaZm2#g&ARkMB@ca7@K55Ppf%7UET^aksK9GtqueAK';
        $this->dsn=$this->typeBDD.":host=".$this->host.";dbname=".$this->dbname;

        $this->connection();
        $this->saveTable();
    }

    // FR: connexion à la base de donnée
    // EN: database connection
    function connection() {
        try {
            $this->pdo = new PDO($this->dsn, $this->username, $this->password);
        } catch (\Throwable $th) {
            $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(001)");
        }
    }
    
    // FR: répertorie les tables de la base de données
    // EN: lists database tables
    function saveTable() {
        try {
            $resultat = $this->pdo->query("SHOW TABLES;");
            $retourSQL = $resultat->fetchAll(PDO::FETCH_COLUMN);
        } catch (\Throwable $th) {
            $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(002)");
        }

        try {
            foreach ($retourSQL as $table) {
                $resultat = $this->pdo->query("SHOW COLUMNS FROM $table;");
                $retourSQL = $resultat->fetchAll(PDO::FETCH_COLUMN);
                $this->tabTable[$table] = $retourSQL;
            }
        } catch (\Throwable $th) {
            $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(003)");
        }
    }

    // FR: retourne la valeur GET lié à ça clé
    // EN: returns the GET value linked to this key
    function attributGET($valeurCle) {
        if (isset($_GET[$valeurCle])) {
            $valeur = $_GET[$valeurCle];
        }
        else {
            $valeur = null;
        }
    
        return $valeur;
    }

    // FR: renvoie le préfixe de la table demandé (vue ou table)
    // EN: returns the prefix of the requested table (view or table)
    function tablePrefix() {
        if (isset($_GET["vue"])) {
            $prefix = "V_";
        }
        else {
            $prefix = "T_";
        }
        return $prefix;
    }

    // FR: renvoie une erreur en JSON
    // EN: returns a JSON error
    function error($strErreur) {
        $this->tabErreur["ERREUR"] = $strErreur;
        echo json_encode($this->tabErreur);
        exit();
    }

    function checkTable($originName) {
        if ($originName === null) {
            $this->error("Aucune donnée n'a été demandé!");
        }
    }

    // FR: vérifie que la table existe en base
    // EN: checks that the table exists in the database
    function checkExistingTable($table) {
        if (!isset($this->tabTable[$table])) {
            $this->error("Les données que vous nous spécifiez son invalide\ncode erreur(004)");
        }
    }

    // FR: vérifie que la table existe en base
    // EN: checks that the table exists in the database
    function checkExistingColumn($table, $column) {
        if (!in_array($column, $this->tabTable[$table])) {
            $this->error("Les données que vous nous spécifiez son invalide!\ncode erreur(005)");
        }
    }

    // FR: renvoie toutes les valeurs de la table ou une si l'id est spécifié
    // EN: returns all table values, or one if id is specified
    function select() {


        try {
            // init
            $originName = $this->attributGET("table");
            $id = $this->attributGET("id");
            $tablePrefix = $this->tablePrefix();

            // FR: si le nom de la table n'est pas précisé alors erreur
            // EN: if table name not specified, then error
            $this->checkTable($originName);
            $tableName = "$tablePrefix$originName";

            // FR: si le nom de la table n'existe pas alors erreur
            // EN: if table name does not exist then error
            $this->checkExistingTable($tableName);

            // FR: construction de la requête SQL
            // EN: SQL query construction
            $reqSQL = "SELECT * FROM $tableName";
            if ($id != null) { 
                $columnId = "Id$originName";
                $reqSQL="$reqSQL\nWHERE $columnId = :id";
            }

            // FR: requête préparé
            // EN: query prepared
            $reqSQLPrepare = $this->pdo->prepare($reqSQL);
            
            // FR: Définit la valeur id
            // EN: Sets id value
            try {
                if ($id != null) { $reqSQLPrepare->bindValue(":id", $id, PDO::PARAM_INT); }
            } catch (\Throwable $th) {
                $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(010)");
            }

            // FR: execute la requête SQL
            // EN: executes the SQL query
            try {
                $reqSQLPrepare->execute();
            } catch (\Throwable $th) {
                $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(011)");
            }

            // FR: recupère les données en JSON
            // EN: recovers data in JSON
            try {
                $retourSQL = json_encode($reqSQLPrepare->fetchAll(PDO::FETCH_ASSOC));
            } catch (\Throwable $th) {
                $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(012)");
            }

        } catch (\Throwable $th) {
            $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(013)");
        }
        
        // FR: retourn les données
        // EN: returns data
        return $retourSQL;
    }


    // FR: insert une ou plusieus valeurs
    // EN: insert one or more values
    function insert() {
        try {
            // init
            $originName = $this->attributGET("table");
            $tableName = "T_$originName";
            $tabInsertColumn = [];
            $tabInsertValue = [];
            $reqSQL = "";
            if (isset($_POST["colonnes"]) && isset($_POST["valeurs"])) {
                try {
                    $columns = json_decode($_POST["colonnes"], true);
                    $values = json_decode($_POST["valeurs"], true);
                } catch (\Throwable $th) {
                    $this->error("La structure des données est incorrecte!");
                }
            } else {
                $this->error("Les valeurs 'colonnes' ou 'valeurs' n'existent pas!");
            }
        
            // FR: si le nom de la table n'est pas précisé, alors erreur
            // EN: if table name not specified, then error
            $this->checkTable($originName);
            $tableName = "T_$originName";
    
            // FR: si le nom de la table n'existe pas, alors erreur
            // EN: if table name does not exist, then error
            $this->checkExistingTable($tableName);

            // FR: vérifie et prépare les colonnes dans la requête SQL
            // EN: checks and prepares columns in the SQL query
            try {
                foreach ($columns as $column => $type) {
                    $this->checkExistingColumn($tableName, $column);
                    $tabInsertColumn[] = $column;
                }
            } catch (\Throwable $th) {
                $this->error("La structure de vos données est incorrecte!");
            }
            $insertColumn = "(" . implode(",",$tabInsertColumn) . ")";

            // FR: construit la requête préparée
            // EN: constructs the prepared query
            foreach ($values as $ind => $data) {
                $newValue = $insertColumn;
                foreach ($data as $column => $value) {
                    $newValue = str_replace($column, ":$column$ind", $newValue);
                }
                $tabInsertValue[] = $newValue;
            }
            $insertValue = implode(",",$tabInsertValue);

            // FR: construction la requête préparée
            // EN: build the prepared query
            $reqSQL = "INSERT INTO $tableName $insertColumn VALUES $insertValue;";
            $reqSQLPrepare = $this->pdo->prepare($reqSQL);

            try {
                // FR: Définit les valeurs
                // EN: Sets values
                foreach ($values as $ind => $data) {
                    foreach ($data as $column => $value) {
                        $this->checkExistingColumn($tableName, $column);
                        switch ($columns[$column]) {
                            case 'STR':
                                $reqSQLPrepare->bindValue(":$column$ind", $value, PDO::PARAM_STR);
                                break;
                            case 'INT':
                                $reqSQLPrepare->bindValue(":$column$ind", $value, PDO::PARAM_INT);
                                break;
                            case 'BOOL':
                                $reqSQLPrepare->bindValue(":$column$ind", $value, PDO::PARAM_BOOL);
                                break;
                            default:
                            $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(021)");
                                break;
                        }
                    }
                }
            } catch (\Throwable $th) {
                $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(022)");
            }

            // FR: execute la requête SQL
            // EN: executes the SQL query
            try {
                $reqSQLPrepare->execute();
            } catch (\Throwable $th) {
                $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(023)");
            }

        } catch (\Throwable $th) {
            $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(024)");
        }

        return "OK";
    }

    function delete() {
        try {
            
            // init
            $originName = $this->attributGET("table");
            $id = $this->attributGET("id");

            // FR: si le nom de la table n'est pas précisé, alors erreur
            // EN: if table name not specified, then error
            $this->checkTable($originName);
            $tableName = "T_$originName";
            $columnId = "Id$originName";

            // FR: si le nom de la table n'existe pas, alors erreur
            // EN: if table name does not exist, then error
            $this->checkExistingTable($tableName);

            // FR: vérifie id
            // EN: check id
            if ($id === null) {
                $this->error("La valeur que vous souhaitez supprimer n'est pas spécifié!");
            }
            elseif($id <= 0){
                $this->error("Il est impossible de supprimer cette valeur!");
            }

            // FR: construction la requête préparée
            // EN: build the prepared query
            $reqSQL = "DELETE FROM $tableName WHERE $columnId = :id";
            $reqSQLPrepare = $this->pdo->prepare($reqSQL);

            try {
                $reqSQLPrepare->bindValue(":id", $id, PDO::PARAM_INT);
            } catch (\Throwable $th) {
                $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(030)");
            }

            try {
                $reqSQLPrepare->execute();
            } catch (\Throwable $th) {
                $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(031)");
            }
        } catch (\Throwable $th) {
            $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(032)");
        }

        return "OK";
    }

    function update() {
        
        try {

            try {
                // FR: récupération des données de la méthode PUT
                // EN: retrieving data from the PUT method
                $putfp = fopen('php://input', 'r');
                $putdata = '';
                $tabValeursDynamique = [];
                while($data = fread($putfp, 1024))
                    $putdata .= $data;
    
                $putdata = explode("\n",$putdata);
                foreach ($putdata as $key => $value) {
                    if (strlen(stristr($value, "-----"))>0 || strlen($value)<=1) {
                        continue;
                    }
                    elseif (strlen(stristr($value, "Content-Disposition: form-data; name=\""))>0) {
                        $variableDynamique = str_replace("Content-Disposition: form-data; name=\"", "", $value);
                        $variableDynamique = str_replace("\"", "", $variableDynamique);
                        continue;
                    }
                    $$variableDynamique = json_decode($value, true);
                    $tabValeursDynamique[] = $$variableDynamique;
                }
                fclose($putfp);
            } catch (\Throwable $th) {
                $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(040)");
            }

            // init
            $columns = $tabValeursDynamique[0];
            $values = $tabValeursDynamique[1];
            $originName = $this->attributGET("table");
            $id = $this->attributGET("id");
            $tabUpdateColumn = [];
            $tabUpdateValue = [];
            $reqSQL = "";

            // FR: si le nom de la table n'est pas précisé, alors erreur
            // EN: if table name not specified, then error
            $this->checkTable($originName);
            $tableName = "T_$originName";
            $columnId = "Id$originName";

            // FR: si le nom de la table n'existe pas, alors erreur
            // EN: if table name does not exist, then error
            $this->checkExistingTable($tableName);

            // FR: vérifie id
            // EN: check id
            if ($id === null) {
                $this->error("La valeur que vous souhaitez modifier n'est pas spécifié!");
            }
            elseif($id <= 0){
                $this->error("Il est impossible de modifier cette valeur!");
            }

            
            // FR: vérifie et prépare les colonnes dans la requête SQL
            // EN: checks and prepares columns in the SQL query
            try {
                foreach ($columns as $column => $type) {
                    $this->checkExistingColumn($tableName, $column);
                    $tabUpdateColumn[] = "$column = :$column";
                }
            } catch (\Throwable $th) {
                $this->error("La structure de vos données est incorrecte!");
            }
            $colonneUpdate = implode(",",$tabUpdateColumn);

            // FR: construction la requête préparée
            // EN: build the prepared query
            $reqSQL = "UPDATE $tableName SET $colonneUpdate WHERE $columnId = :id;";
            $reqSQLPrepare = $this->pdo->prepare($reqSQL);

            try {
                $reqSQLPrepare->bindValue(":id", $id, PDO::PARAM_INT);    
            } catch (\Throwable $th) {
                $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(041)");
            }

            try {
                // FR: Définit les valeurs
                // EN: Sets values
                foreach ($values as $ind => $data) {
                    foreach ($data as $column => $value) {
                        $this->checkExistingColumn($tableName, $column);
                        switch ($columns[$column]) {
                            case 'STR':
                                $reqSQLPrepare->bindValue(":$column", $value, PDO::PARAM_STR);
                                break;
                            case 'INT':
                                $reqSQLPrepare->bindValue(":$column", $value, PDO::PARAM_INT);
                                break;
                            case 'BOOL':
                                $reqSQLPrepare->bindValue(":$column", $value, PDO::PARAM_BOOL);
                                break;
                            default:
                            $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(042)");
                                break;
                        }
                    }
                }
            } catch (\Throwable $th) {
                $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(042)");
            }
            
            // FR: execute la requête SQL
            // EN: executes the SQL query
            try {
                $reqSQLPrepare->execute();
            } catch (\Throwable $th) {
                $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(043)$th")
            }

        } catch (\Throwable $th) {
            $this->error("C'est pas vous c'est nous.\nErreur interne: code erreur(044)");
        }

        return "OK";
    }

}

?>
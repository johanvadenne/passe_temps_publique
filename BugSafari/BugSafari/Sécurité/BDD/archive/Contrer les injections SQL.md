## PHP
### Requête préparer
**Exemple:**
```php
$this->pdo = new PDO($this->dsn, $this->username, $this->password);
$reqSQLPrepare = $this->pdo->prepare($reqSQL);
$reqSQLPrepare->bindValue(":id", $id, PDO::PARAM_INT);
$reqSQLPrepare->execute();
$retourSQL = json_encode($reqSQLPrepare->fetchAll(PDO::FETCH_ASSOC));
```
*info:* plus de détaille dans le fichier `BDD.php` de l'API
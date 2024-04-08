<?php

include("./BDD.php");

$BOT_VEILLE = new BDD;

// methode
switch ($_SERVER['REQUEST_METHOD']) {
    case 'GET':
        $dataJSON = $BOT_VEILLE->select();
        echo $dataJSON;
        break;
    case 'POST':
        $dataJSON = $BOT_VEILLE->insert();
        echo $dataJSON;
        break;
    case 'DELETE':
        $dataJSON = $BOT_VEILLE->delete();
        echo $dataJSON;
        break;
    case 'PUT':
        $dataJSON = $BOT_VEILLE->update();
        echo $dataJSON;
        break;
    default:
        echo "aucune méthode valide";
        break;
}
?>
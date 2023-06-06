<?php
#je définie une variable
$a = 0;

#je créer une boucle
while (1) {

    #je demande de rentrer un élève
    echo"Saisissé un élève (écrivé STOP pour arrêter):\n";

    #j'enregistre l'élève dans une varable
    $eleve = readline();

    #si la saisi est égale a STOP, arrêterla boucle
    if ("STOP" == $eleve) {
        break;
    }

    #j'enregistre dans le tableau l'élèvre
    $class[$a] = $eleve;

    #j'ajoute 1 à la variable $a
    $a = $a + 1;
}

#j'attribue à la variable le nombre de mot que j'ai dans le tableau
$tableau = sizeof($class) - 1;
#je présente tous les élèves enregistrés
for ($i=0; $i <= $tableau; $i++) { 
    echo("$class[$i]\n");
}

#j'écris un élève au hasrad
echo "\nvoici un élève au hasard: ". $class[rand(0, $tableau)]. "\n \n";

#j'écris tous les élèves en majuscule
for ($i=0; $i <= $tableau; $i++) { 
    echo(strtoupper("$class[$i]\n \n"));
}

#je mélange le tableau
shuffle($class);

#je présente tous les élèves enregistrés
for ($i=0; $i <= $tableau; $i++) { 
    echo("$class[$i]\n");
}
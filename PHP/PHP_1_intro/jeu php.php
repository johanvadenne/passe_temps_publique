<?php

#Jeu php

#intro
echo("Bonjour! bienvenue sur un jeu php! \nCe jeu consiste à tuer son adversaire en premier. \nCe jeu se joue tour par tour et vous pouvez effectuer une action. \n Il y a plusieur type de d'action : \n- Soins : Vous pouvez vous soignez (entre 1PV et 10PV) \n- Attaque : Vous pouvez attaquer votre adversaire (entre 1PV et 10PV) \nVous avez chacun 100PV \nBonne chance!!!\n");

#constante
define("JOUEUR1", 100);
define("JOUEUR2", 100);

#variable
$reponse = "";
$PVjoueur1 = JOUEUR1;
$PVjoueur2 = JOUEUR2;
$attaque = 0;
$soins = 0;
$perdu = "";
$gagner = "";
$joueur1 = "";
$joueur2 = "";
#joueur 1
while(true)
{
    echo("Joueur 1 comment vous vous appelez :\n");
    $joueur1 = readline();
    echo("Joueur 1 : $joueur1 \nVoulez vous changer? \n- OUI (1)\n- NON (2)\n");
    $reponse = readline();
    if ($reponse == "2") {
        break;
    }
}

$reponse = "";

#joueur 2
while(true)
{
    echo("Joueur 2 comment vous vous appelez :\n");
    $joueur2 = readline();
    echo("Joueur 2 : $joueur2 \nVoulez vous changer? \n- OUI \n- NON \n");
    $reponse = readline();
    if ($reponse == "2") {
        break;
    }
}

#action
while(true)
{

    $reponse = "";

    while(true){
        echo("$joueur1 : vous avez $PVjoueur1 PV \nà vous de jouer :\n- ATTAQUER (1) \n- SOINS (2)\n");
        $reponse = readline();
        if ($reponse == "1") {
            $attaque = rand(1, 10);
            $PVjoueur2 = $PVjoueur2 - $attaque;
            echo("$joueur1 attaque $joueur2! \n$joueur2 perd $attaque PV!\n");
            break;
        }
        elseif ($reponse == "2") {
            $soins = rand(1, 10);
            $PVjoueur1 = $PVjoueur1 + $soins;
            echo("$joueur1 se soigne de $soins PV\n");
            break;
        }
    }

    if ($PVjoueur1 <= 0){
        $perdu = $joueur1;
        $gagner = $joueur2;
        break;
    }
    elseif ($PVjoueur2 <= 0){
        $perdu = $joueur2;
        $gagner = $joueur1;
        break;
    }

    $reponse = "";

    while(true){
        echo("$joueur2 : vous avez $PVjoueur2 PV \nà vous de jouer :\n- ATTAQUER (1) \n- SOINS (2)\n");
        $reponse = readline();
        if ($reponse == "1") {
            $attaque = rand(1, 10);
            $PVjoueur1 = $PVjoueur1 - $attaque;
            echo("$joueur2 attaque $joueur1! \n$joueur1 perd $attaque PV!\n");
            break;
        }
        elseif ($reponse == "2") {
            $soins = rand(1, 10);
            $PVjoueur2 = $PVjoueur2 + $soins;
            echo("$joueur2 se soigne de $soins PV\n");
            break;
        }
    }

    if ($PVjoueur1 <= 0){
        $perdu = $joueur1;
        $gagner = $joueur2;
        break;
    }
    elseif ($PVjoueur2 <= 0){
        $perdu = $joueur2;
        $gagner = $joueur1;
        break;
    }
}

echo("$perdu n'a plus de vie! \n $gagner remporte cette partie! \n merci d'avoir joué!");
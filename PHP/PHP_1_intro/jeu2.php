<?php

#variable
$reponse = "";

#perso 1
$PVsorcier = 80;
$attaque_1 = 0;
$foudre = 0;
$feu = 0;
$poison = 0;

#perso 2
$PVguérisseuse = 120;
$attaque_2 = 0;
$soins = 0;
$sois_collectif = 0;
$vol_energie_vitale = 0;

#perso 3
$PVchevalier = 100;
$coup_epee = 0;
$bouclier = 0;
$tour_bouclier = 0;
$parade = 0;
$tournade = 0;

#slime
$PVslime_1 = 50;
$PVslime_2 = 50;
$PVslime_3 = 50;
$charge = 0;
$boule_de_slime = 0;
$regeneration = 0;

#level1
while (true) {
    echo("Perso chevalier:\n- COUP D'EPEE dégat: (5PV à 10PV) [1]\n- BOUCLIER défence: (30% à 40% 3 tour) [2]\n- PARADE chance: (33%) réussie: (double les dégats) [3]\n");
    $reponse = readline();
    if ($reponse == "1") {
        $reponse = "";
        $coup_epee = rand(5,10);
        
        $reponse = "";
        while (true){
            echo("Quel monstre voulez vous attaquer:\n");
            if ($PVslime_1 > 0){
                echo("SLIM 1: $PVslime_1 PV [1]\n");
            }
            if ($PVslime_2 > 0){
                echo("SLIM 2: $PVslime_2 PV [2]\n");
            }
            if ($PVslime_3 > 0){
                echo("SLIM 3: $PVslime_3 PV [3]\n");
            }
            $reponse = readline();
            if ($reponse == "1") {
                if ($PVslime_1 > 0) {
                    break;
                    
                }
                else{
                    echo("Le slime 1 est mort\n");
                }
            }
            if ($reponse == "2") {
                if ($PVslime_2 > 0) {
                    break;
                    
                }
                else{
                    echo("Le slime 2 est mort\n");
                }
            }
            if ($reponse == "3") {
                if ($PVslime_3 > 0) {
                    break;
                    
                }
                else{
                    echo("Le slime 3 est mort\n");
                }
            }
        }
        
        if ($reponse == "1") {
            $PVslime_1 = $PVslime_1 - $coup_epee;
            echo("Le slim 1 à subie $coup_epee dégats\n");
            if ($PVslime_1 <= 0) {
                echo("Le slime 1 a été éliminé!\n");
            }
        }
        if ($reponse == "2") {
            $PVslime_2 = $PVslime_2 - $coup_epee;
            echo("Le slim 2 à subie $coup_epee dégats\n");
            if ($PVslime_2 <= 0) {
                echo("Le slime 2 a été éliminé!\n");
            }
        }
        if ($reponse == "3") {
            $PVslime_3 = $PVslime_3 - $coup_epee;
            echo("Le slim 3 à subie $coup_epee dégats\n");
            if ($PVslime_3 <= 0) {
                echo("Le slime 3 a été éliminé!\n");
            }
        }
        $reponse = "";
    }

    if ($reponse = "2") {
        $bouclier = rand(0.6,0.7);
        $tour_bouclier = 3;
    }

    if ($reponse = "3") {
        # code...
    }

    if ($PVslime_1 <= 0 && $PVslime_2 <= 0 && $PVslime_3 <= 0) {
        break;
    }
}

echo("BRAVO!!! Vous avez gagné le 1er niveau");
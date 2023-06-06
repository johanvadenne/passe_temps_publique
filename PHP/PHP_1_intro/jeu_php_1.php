<?php

#variable
$repoonse = "";
$joueur1 = "";
$joueur2 = "";
$PVjoueur1 = 0;
$PVjoueur2 = 0;
$attaque_joueur1 = "";
$ATTAQUE1_joueur1 = 0;
$ATTAQUE2_joueur1 = 0;
$ATTAQUE3_joueur1 = 0;
$SUPER_ATTAQUE3_joueur1 = 0;
$attaque_joueur2 = "";
$ATTAQUE1_joueur2 = 0;
$ATTAQUE2_joueur2 = 0;
$ATTAQUE3_joueur2 = 0;
$SUPER_ATTAQUE3_joueur2 = 0;

#perso
$chevalier = 100;
$ATTAQUEchevalier = "- COUP D'EPEE [1]\n- CONTRE ATTAQUE [2]\n- BOUCLIER [3]\n";
$magicien = 80;
$ATTAQUEmagicien = "- FEU [1]\n- FOUDRE [2]\n- POISON [3]\n";
$archer = 90;
$ATTAQUEarcher = "- TIR A L'ARC [1]\n- TIR PRECIS [2]\n- AGILITER [3]\n";
$golem = 120;
$ATTAQUEgolem = "- COUP DE PIERRE [1]\n- RENFORCEMENT [2]\n- TRANBLEMENT DE TERRE [3]\n";
$soigneur = 120;
$ATTAQUEsoigneur = "- SOINS [1]\n- VOL D'ENERGIE VITAL [2]\n- AFAIBLISSEMENT [3]\n";

#capacité
#chevalier
$coup_epee = 0;
$contre_attaque = 0;
$bouclier = 0;
$lame_tranchant = 0;

#magicien
$feu = 0;
$foudre = 0;
$poison = 0;
$glace = 0;

#archer
$tir_a_l_arc = 0;
$tir_precis = 0;
$agilite = 0;
$multi_tir = 0;

#golem
$coup_de_pierre = 0;
$renforcement = 0;
$tranblement_terre = 0;
$appelle_aux_cailloux = 0;

#soigneur
$soins = 0;
$vol_energie_vitale = 0;
$afaiblissement = 0;
$super_soins = 0;

#fonction
function perso1($a,$b,$c,$d,$e,$f){
    #chevalier
    $coup_epee = rand(5,10);
    $contre_attaque = rand(0,3);
    $bouclier = rand(0.8,0.70);
    $lame_tranchant = rand(7,15);

    #magicien
    $feu = rand(6,11);
    $foudre = rand(3,8);
    $poison = rand(1,3);
    $glace = (0.5);

    #archer
    $tir_a_l_arc = rand(5,10);
    $tir_precis = rand(2,5 );
    $agilite = 0;
    $multi_tir = 0;

    #golem
    $coup_de_pierre = 0;
    $renforcement = 0;
    $tranblement_terre = 0;
    $appelle_aux_cailloux = 0;

    #soigneur
    $soins = 0;
    $vol_energie_vitale = 0;
    $afaiblissement = 0;
    $super_soins = 0;

    $PVjoueur1 = $a;
    $ATTAQUE1_joueur1 = $b;
    $ATTAQUE2_joueur1 = $c;
    $ATTAQUE3_joueur1 = $d;
    $SUPER_ATTAQUE3_joueur1 = $e;
    $attaque_joueur1 = $f;
}

function perso2($a,$b,$c,$d,$e,$f){
    $PVjoueur2 = $a;
    $ATTAQUE1_joueur2 = $b;
    $ATTAQUE2_joueur2 = $c;
    $ATTAQUE3_joueur2 = $d;
    $SUPER_ATTAQUE3_joueur2 = $e;
    $attaque_joueur2 = $f;
}
#nom joueur 1
while (true) {
    echo("Joueur 1, entrer votre nom:\n");
    $joueur2 = readline();
    if ($joueur2 != "") {
        echo("Voulez vous changer?\n- NON [1]\n- OUI [2]\n");
        $repoonse = readline();
    }
    if ($reponse == "1") {
        break;
    }
}

#nom joueur 2
while (true) {
    echo("Joueur 1, entrer votre nom:\n");
    $joueur2 = readline();
    if ($joueur2 != "") {
        echo("Voulez vous changer?\n- NON [1]\n- OUI [2]\n");
        $repoonse = readline();
    }
    if ($reponse == "1") {
        break;
    }
}

#personnage joueur 1
while (true) {
    echo("$joueur2 choisissé votre personnage:\n- CHEVALIER [1]\n- MAGICIEN [2]\n- ARCHER [3]\n- GOLEM [4]\n- SOIGNEUR [5]\n");
    $repoonse = readline();
    if ($repoonse = "1") {
        perso1($chevalier, $coup_epee, $contre_attaque, $bouclier, $lame_tranchant, $ATTAQUEchevalier);
    }
    elseif ($repoonse = "2") {
        perso1($magicien, $feu, $foudre, $poison, $glace, $ATTAQUEchevalier);
    }
    elseif ($repoonse = "3") {
        perso1($archer, $tir_a_l_arc, $tir_precis, $agilite, $multi_tir, $ATTAQUEarcher);
    }
    elseif ($repoonse = "4") {
        perso1($golem, $coup_de_pierre, $renforcement, $tranblement_terre, $appelle_aux_cailloux, $ATTAQUEgolem);
    }
    elseif ($repoonse = "5") {
        perso1($soigneur, $soins, $vol_energie_vitale, $afaiblissement, $super_soins, $ATTAQUEsoigneur);
    }

    echo("Voulez vous changer?\n- NON [1]\n- OUI [2]\n");
    $repoonse = readline();
    if ($repoonse = "1") {
        break;
    }
}


#personnage joueur 2
while (true) {
    echo("$joueur2 choisissé votre personnage:\n- CHEVALIER [1]\n- MAGICIEN [2]\n- ARCHER [3]\n- GOLEM [4]\n- SOIGNEUR [5]\n");
    $repoonse = readline();
    if ($repoonse = "1") {
        perso2($chevalier, $coup_epee, $contre_attaque, $bouclier, $lame_tranchant, $ATTAQUEchevalier);
    }
    elseif ($repoonse = "2") {
        perso2($magicien, $feu, $foudre, $poison, $glace, $ATTAQUEchevalier);
    }
    elseif ($repoonse = "3") {
        perso2($archer, $tir_a_l_arc, $tir_precis, $agilite, $multi_tir, $ATTAQUEarcher);
    }
    elseif ($repoonse = "4") {
        perso2($golem, $coup_de_pierre, $renforcement, $tranblement_terre, $appelle_aux_cailloux, $ATTAQUEgolem);
    }
    elseif ($repoonse = "5") {
        perso2($soigneur, $soins, $vol_energie_vitale, $afaiblissement, $super_soins, $ATTAQUEsoigneur);
    }

    echo("Voulez vous changer?\n- NON [1]\n- OUI [2]\n");
    $repoonse = readline();
    if ($repoonse = "1") {
        break;
    }
}

#gameplay
while ($PVjoueur1 > 0 || $PVjoueur2 > 0) {
    echo("$joueur1 à vous de jouer");
}
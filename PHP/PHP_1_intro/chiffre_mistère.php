<?php
#je definie une constante
define("CHIFFRE", rand( 0, 10));
define("CHANCE", 3);

#je presente le jeu
print "BIENVENUE SUR PHP LOTO!!!\nVous aurrez 3 chance pour trouver le chiffre mistère!\nNous vous guiderons si le chiffre est suppérieur ou inférieur lors de vos tentatives!\nLe chiffre est entre 0 et 10!\nA vous de jouer!\n\n";

#boucle
for ($i=0; $i < CHANCE; $i++) { 

    #choisir un chiffre
    print "choisissez votre chiffre:\n";
    $tentative = trim(fgets(STDIN));

    #si le chiffre est trouver
    if ($tentative == CHIFFRE) {
        $i = 4;
        print "BRAVO!!! vous avez remporté le jackpot de php loto!!!\n";
    }

    #si le chiffre est inferieur
    elseif($tentative < CHIFFRE) {
        $t = $i + 1;
        print "votre chiffre est supérieur à $tentative!\n
        Retentez votre chance, vous avez fait $t tentative(s)!\n";
    }

    #si le chiffre est superieur
    else {
        $t = $i + 1;
        print "votre chiffre est inférieur à $tentative!\n
        Retentez votre chance, vous avez fait $t tentative(s)!\n";
    }
}

#si il a perdu
if ($i == 3) {
    print "Dommage... le chiffre était ☞ ".CHIFFRE. " rententez votre chance, c'est GRATUIT!!!";
}
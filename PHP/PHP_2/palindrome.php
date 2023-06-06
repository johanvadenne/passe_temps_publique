<?php


//saisie
echo "Choisissé une phrase palindrome\n";
//enregistre saisie
$SaisiePalindrome = readline();
//appelle fonction
$MonPalindrome = Palindrome($SaisiePalindrome);

//fonction qui teste les palindromes
function Palindrome(string $Palindrome) : bool
{
    //constante
    define ("PARASITE",[",","."," ","'",'"',"#","&","~","{","}","[","]","-","|","`","_","\\","@","°","(",")","/",";","!",":","?"]);
    define ("NOMBREPARASITE", count(PARASITE));

    //retire les PARASITES
    for ($i=0; $i < NOMBREPARASITE; $i++) { 
        $Palindrome = str_replace(PARASITE[$i], "", $Palindrome);
    }

    //retire les lettres avec accent
    $Palindrome = str_replace("à", "a", $Palindrome);
    $Palindrome = str_replace("é", "e", $Palindrome);
    $Palindrome = str_replace("è", "e", $Palindrome);
    $Palindrome = str_replace("ê", "e", $Palindrome);
    $Palindrome = str_replace("ç", "c", $Palindrome);
    $Palindrome = str_replace("ô", "o", $Palindrome);
    $Palindrome = str_replace("û", "u", $Palindrome);
    $Palindrome = str_replace("ï", "i", $Palindrome);

    //teste palindrome
    if (strrev($Palindrome) == $Palindrome) {
        $Booleen = True;
    }
    else{
        $Booleen = False;
    }
    return $Booleen;
}

//phrase de fin si oui ou non palindrome
if ($MonPalindrome){
    echo "Ceci est bien un palindrome\n";
}
else
{
    echo"Ceci n'est pas un palindrome\n";
}
const menuOnglet = document.getElementById("menu_onglet");
const ongletLienAccueil = document.getElementById("onglet_lien_accueil");
const ongletLienEvenement = document.getElementById("onglet_lien_evenement");
const ongletLienGalerie = document.getElementById("onglet_lien_galerie");
const ongletLienMembre = document.getElementById("onglet_lien_membre");
const ongletLienContact = document.getElementById("onglet_lien_contact");
const ongletLienLesbonnesAdresses = document.getElementById("onglet_lien_les_bonnes_adresses");
const ongletLienAccueilANePasManquer = document.getElementById("onglet_lien_a_ne_pas_manquer");
const aPropos = document.getElementById("a_propos");
const unProbleme = document.getElementById("un_probleme");
const corpNavigation = document.getElementById("corp_navigation");

const TaiileOngletMenuOuvert = 15;
const TaiileOngletMenuFermer = 2.75;
var ongletMenuOuvert = false;
const ongletLienImage = [
    {
        elementHTML: ongletLienAccueil,
        image: "./assets/images/frelots/accueil.png",
        texte: "<b>ACCEUIL</b>"
    },
    {
        elementHTML: ongletLienEvenement,
        image: "./assets/images/frelots/evenement.png",
        texte: "<b>EVENEMENTS</b>"
    },
    {
        elementHTML: ongletLienGalerie,
        image: "./assets/images/frelots/galerie.png",
        texte: "<b>GALERIE</b>"
    },
    {
        elementHTML: ongletLienMembre,
        image: "./assets/images/frelots/membre.png",
        texte: "<b>MEMBRES</b>"
    },
    {
        elementHTML: ongletLienContact,
        image: "./assets/images/frelots/contact.png",
        texte: "<b>CONTACT</b>"
    },
    {
        elementHTML: ongletLienLesbonnesAdresses,
        image: "./assets/images/frelots/les_bonnes_adresses.png",
        texte: "<b>LES BONNES ADRESSES</b>"
    },
    {
        elementHTML: ongletLienAccueilANePasManquer,
        image: "./assets/images/frelots/a_ne_pas_manquer.png",
        texte: "<b>A NE PAS MANQUER</b>"
    },
    {
        elementHTML: aPropos,
        image: "./assets/images/frelots/a_propos.png",
        texte: "à propos du site"
    },
    {
        elementHTML: unProbleme,
        image: "./assets/images/frelots/un_probleme.png",
        texte: "un problème?"
    }
]


function ouvreMenu(){
    if (ongletMenuOuvert) {
        menuOnglet.style.width = TaiileOngletMenuFermer+"%";
        corpNavigation.style.width = 100-TaiileOngletMenuFermer+"%";
        corpNavigation.style.marginLeft = TaiileOngletMenuFermer+"%";
        modifieOngletLienEnImage(true);
        
    }
    else {
        menuOnglet.style.width = TaiileOngletMenuOuvert+"%";
        corpNavigation.style.width = 100-TaiileOngletMenuOuvert+"%";
        corpNavigation.style.marginLeft = TaiileOngletMenuOuvert+"%";
        let interval = setInterval(function() {
            modifieOngletLienEnImage(false);
            clearInterval(interval);
        },150)
    }
    ongletMenuOuvert = !ongletMenuOuvert;
}

function modifieOngletLienEnImage(modifierEnImage) {
    if (modifierEnImage) {
        ongletLienImage.forEach(function(item) {
            const elementHTML = item.elementHTML;
            const image = item.image;
            elementHTML.innerHTML = "<img src=\""+image+"\">";
        });
    }
    else {
        ongletLienImage.forEach(function(item) {
            const elementHTML = item.elementHTML;
            const texte = item.texte;
            elementHTML.innerHTML = texte;
        });
    }
}

menuOnglet.style.width = TaiileOngletMenuFermer+"%";
corpNavigation.style.width = 100-TaiileOngletMenuFermer+"%";
corpNavigation.style.marginLeft = TaiileOngletMenuFermer+"%";
modifieOngletLienEnImage(true);
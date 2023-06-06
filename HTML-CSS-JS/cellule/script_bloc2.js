// FR: element bulle
const elementBulle = [
    { id: "IPV4", positionLeft: "200px", positionTop: "400px", taille: "160px", txt: "<p class=\"close\" id=\"close\">✖</p><h1>IPV4</h1><h2>description:</h2><p>    L’IPv4, pour Internet Protocol version 4, est utilisé depuis 1983 pour permettre à internet de fonctionner :    chaque terminal sur le réseau internet (ordinateur, téléphone, serveur etc.) est adressable par une adresse    IPv4.    Le protocole IPv4 offre un espace d'adressage de près de 4,3 milliards d'adresses IPv4. Or, le succès    d'internet,    la diversité des usages et la multiplication des objets connectés ont comme conséquence directe l'épuisement    progressif des adresses IPv4,    certaines régions du monde étant touchées plus que d'autres. Les quatre principaux opérateurs français    (Bouygues Telecom, Free, Orange, SFR)    ont déjà affecté entre 88% et 99% des adresses IPv4 qu’ils possèdent, à fin juin 2018.</p><h2>Représentation:</h2><p>    Une adresse IPv4 est représentée sous la forme de quatre nombres entiers séparés par des points comme    193.43.55.67.    Chacun des nombres représente un octet. La plage d'attribution s'étend de 0.0.0.0 à 255.255.255.255,    sachant qu'il existe des contraintes empêchant l'utilisation de certaines adresses (réservée, masque,    broadcast, etc.)</p><img src=\"image/bloc2/ipv4.png\"><h2>Les classes</h2><p>Chaque adresse IP appartient à une classe qui correspond à une plage d’adresses IP.Il y à 5 classes en tout les classes, A, B, C, D et E.Le fait d’avoir des classes d’adresses permet d’adapter l’adressage selon la taille du réseau.</p><table class=\"table_classe\">    <tr>        <th>Classe</th>        <th>Bits de départ</th>        <th>Début</th>        <th>Fin</th>        <th>Notation CIDR par défaut</th>        <th>Masque de sous-réseaupar défaut</th>    </tr>    <tr>        <td>Classe A</td>        <td>0</td>        <td>0.0.0.0</td>        <td>126.255.255.255</td>        <td>/8</td>        <td>255.0.0.0</td>    </tr>    <tr>        <td> Classe B</td>        <td>10</td>        <td>128.0.0.0</td>        <td>191.255.255.255</td>        <td>/16</td>        <td>255.255.0.0</td>    </tr>    <tr>        <td>Classe C</td>        <td>110</td>        <td>192.0.0.0</td>        <td>223.255.255.255</td>        <td>/24</td>        <td>255.255.255.0</td>    </tr>    <tr>        <td>Classe D</td>        <td>1110</td>        <td>224.0.0.0</td>        <td>239.255.255.255</td>        <td></td>        <td>255.255.255.255</td>    </tr>    <tr>        <td>Classe E (réservée)</td>        <td>1111</td>        <td>240.0.0.0</td>        <td>255.255.255.255</td>        <td></td>        <td>non défini</td>    </tr></table><h1>IPV6</h1><h2>description:</h2><p>    La version précédente, IPv4, utilise un schéma d’adressage de 32 bits pour prendre en charge 4,3 milliards de dispositifs.     Ce qui était considéré comme suffisant à l’époque de sa mise en œuvre.     Cependant, depuis le début des années 90, avec la croissance de l’internet, des ordinateurs personnels,     des smartphones et maintenant de l’internet des objets, il est devenu évident que le monde avait besoin de plus d’adresses.     Le nombre de machines et de connexions a littéralement explosé.<br>    <br>    Heureusement, l’Internet Engineering Task Force (IETF) l’a compris il y a près de 25 ans. En 1998, il a créé l’IPv6,     qui utilise plutôt l’adressage 128 bits pour prendre en charge environ 340 trillions de trillions.     Au lieu de la méthode d’adressage IPv4, qui consiste en quatre ensembles de chiffres de un à trois chiffres,     IPv6 utilise huit groupes de quatre chiffres hexadécimaux, séparés par des deux points.</p><h2>Représentation:</h2><p>    Une adresse IPv6 ressemble à ceci : 2620:cc:8000:1c82:532c:cc2e:f2fa:5a9b. Au lieu de quatre chiffres, il y en a huit,     et ils sont séparés par des deux-points plutôt que par des virgules. Elle repose sur un format EUI-64 modifié.     Ce format EUI-64 pourrait permettre à des tiers de tirer des conclusions sur l’adresse MAC.     Il repose sur la conversion du format d’adresse MAC standard au format EUI-64 modifié.</p><img src=\"image/bloc2/ipv6.png\">" },
    { id: "modele_OSI", positionLeft: "500px", positionTop: "200px", taille: "200px", txt: "<p class=\"close\" id=\"close\">✖</p><h1>Le modèle OSI</h1><h2>description:</h2><p>    La chose la plus importante à comprendre sur les aspects de réseau est le modèle OSI car c'est la norme de communication pour tous les systèmes informatiques.     Il est divisé en 7 couches empilées les unes sur les autres. Elles peuvent communiquer avec celles du dessus ou celles d'en dessous d'elle-même.</p><img src=\"image/bloc2/model_osi.png\">" }
]

var elementClose
var bulleAffiche = false

// FR: pour chaque élément bulle
elementBulle.forEach(({ id, positionLeft, positionTop, taille, txt }) => {

    const bulle = document.getElementById(id);

    // FR: définit la taille et la position de la bulle
    bulle.style.left = positionLeft;
    bulle.style.top = positionTop;
    bulle.style.width = taille;
    bulle.style.height = taille;

    // FR: si bulle clicker, afficher le text auquelle elle est lié
    bulle.addEventListener("click", function(event) {

        // FR: empêche l'évènement de la balise à et récupère le fichier lié à la bulle 
        event.preventDefault();
        fetch(this.href);

        // FR: récupère les éléments
        const menuBulle = document.querySelector(".menu_bulle")
        const body = document.querySelector(".menu_bloc2")
        const affichageBulle = document.querySelector(".affichage_bulle")

        // FR: crée une animation d'affichage
        body.style.overflow = "auto"
        menuBulle.style.opacity = "0"
        menuBulle.style.Zindex = "-1"
        menuBulle.style.visibility = "hidden"
        affichageBulle.style.opacity = "1"
        affichageBulle.style.Zindex = "1"
        affichageBulle.style.transition = "all 1s ease-in-out"
        affichageBulle.innerHTML = txt
        const x = affichageBulle.getBoundingClientRect();
        setTimeout(() => {
            affichageBulle.style.height = "0px"
        }, 100);
        const sousElements = document.querySelectorAll('.affichage_bulle *');
        for (let i = 0; i < sousElements.length; i++) {
            sousElements[i].style.opacity = "0";
        }
        setTimeout(() => {
            affichageBulle.style.height = x.height + "px"
            setTimeout(() => {
                for (let i = 0; i < sousElements.length; i++) {
                    sousElements[i].style.transition = "opacity 0.5s ease-in-out"
                    sousElements[i].style.opacity = "1";
                }
            }, 600);
        }, 200);
        closeAffichage()
    })
})

function closeAffichage() {
    const elementClose = document.getElementById("close")
    const sousElements = document.querySelectorAll('.affichage_bulle *');
    const affichageBulle = document.querySelector(".affichage_bulle")
    const menuBulle = document.querySelector(".menu_bulle")
    const body = document.querySelector(".menu_bloc2")

    elementClose.addEventListener("click", function() {
        for (let i = 0; i < sousElements.length; i++) {
            sousElements[i].style.opacity = "0";
            closeAffichage()
        }
        setTimeout(() => {
            affichageBulle.style.height = "0px"
            body.style.overflow = "hidden"
            setTimeout(() => {
                affichageBulle.style.opacity = "0"
                setTimeout(() => {
                    menuBulle.style.visibility = "visible"
                    menuBulle.style.opacity = "1"
                    affichageBulle.innerHTML = ""
                    affichageBulle.style.height = "auto"
                }, 600);
            }, 400);
        }, 200);
        return
    })

}
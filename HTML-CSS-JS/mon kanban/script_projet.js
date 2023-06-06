// FR: éléments taches
const idElementBlocTacheProjet = [
    { nomIdElement: "tache_les_frelots", idElement: "#tache_les_frelots", saisie: false, position: 1 },
    { nomIdElement: "tache_mon_site", idElement: "#tache_mon_site", saisie: false, position: 1 },
    { nomIdElement: "tache_INFINITY_FLOORS", idElement: "#tache_INFINITY_FLOORS", saisie: false, position: 1 }
]

// FR: les différentes sections
const idSectionProjet = [
    { nomIdSection: "a_faire", idSection: "#a_faire", nbrTache: 1 },
    { nomIdSection: "en_cours", idSection: "#en_cours", nbrTache: 1 },
    { nomIdSection: "fini", idSection: "#fini", nbrTache: 1 }
]

// FR: initialisation variables
var xDefaut
var yDefaut
var positionSourisDefinit = false
var positionSection
var positionTache
var Tachetop
var tacheLeft
var x
var y

// FR: déplacement du bloc de tâche
idElementBlocTacheProjet.forEach(({ nomIdElement, idElement, saisie, position }) => {
    let element = document.querySelector(idElement);

    // FR: si l'élément tache est pressé
    element.addEventListener("mousedown", function () {
        saisie = true;
        element.style.transition = "box-shadow 0.1s linear";
    });

    // FR: si pression souris levé
    element.addEventListener("click", function (event) {
        idSectionProjet.forEach(({ nomIdSection, idSection, nbrTache }) => {

            element.style.transition = "all 0.1s ease-in-out";

            // FR: récupère la position de la section
            const elementSection = document.querySelector(idSection);
            positionSection = elementSection.getBoundingClientRect();
            mouseX = event.clientX;
            mouseY = event.clientY;
            // récupère l'élément dont vous voulez trouver l'ID parent
            const monElement = document.getElementById(nomIdElement);
            // récupère l'ID parent de l'élément
            let idParent = monElement.parentNode.id;
            const section1 = idSectionProjet.find(s => s.nomIdSection === nomIdSection);
            const section2 = idSectionProjet.find(s => s.nomIdSection === idParent);

            // FR: si souris dans la section
            if (mouseX > positionSection.left && mouseY > positionSection.top && mouseX < (positionSection.left + positionSection.width) && mouseY < (positionSection.top + positionSection.height) && section1.idSection != section2.idSection) {

                console.log(nbrTache)
                const elementTache = document.querySelector(idElement);
                positionTache = elementTache.getBoundingClientRect();
                x = ((positionTache.left) - (positionSection.left)) - ((positionTache.width) * 0.025)
                y = y - (positionTache.height * (nbrTache)) + (positionTache.height * (position-1)) + ((positionTache.width) * 0.025)
                section1.nbrTache += 1;
                section2.nbrTache -= 1;
                const elementT = idElementBlocTacheProjet.find(s => s.nomIdElement === nomIdElement);
                elementT.position = section1.nbrTache

                var monDiv = document.getElementById(nomIdSection);
                var monDiv2 = document.getElementById(nomIdElement);

                // FR: Ajouter le nouvel élément comme enfant de monDiv
                monDiv.appendChild(monDiv2);

                // FR: remet l'élément à sa place pour donner l'illusion que la tache ce glisse dans la section
                element.style.left = x + "px";
                element.style.top = y + "px";

            }

            // FR: réinitializes variables
            saisie = false;
            positionSourisDefinit = false;

            // FR: replacement de l'élément
            element.style.zIndex = "0";
            setTimeout(() => {
                element.style.boxShadow = "0 5px 0px rgba(0, 0, 0, 0.3)";
                element.style.left = "0px"
                element.style.top = "0px"

            }, 1);
        });
    });

    // FR: Si la souris bouge
    document.addEventListener("mousemove", function (event) {

        // FR: Si une tâche est saisie
        if (saisie) {

            // FR: récupère la tâche
            const element = document.querySelector(idElement);

            // FR: si la position de la souris n'est pas positionner pas défaut
            if (!positionSourisDefinit) {
                xDefaut = event.clientX;
                yDefaut = event.clientY;
                positionSourisDefinit = true;
            }

            // FR: récupère la position de la souris
            var xSouris = event.clientX;
            var ySouris = event.clientY;

            // FR: calcule la position de la tâche
            x = (xSouris - xDefaut);
            y = (ySouris - yDefaut);
            element.style.boxShadow = "0 30px 5px rgba(0, 0, 0, 0.3)"
            element.style.zIndex = "1"
            element.style.left = x + "px";
            element.style.top = y + "px";
        }
    });
});
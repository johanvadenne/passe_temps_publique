// FR: éléments taches
const idElementBlocTacheProjet = [
    { nomIdElement: "tache_les_frelots", idElement: "#tache_les_frelots", saisie: false },
    { nomIdElement: "tache_mon_site", idElement: "#tache_mon_site", saisie: false },
    { nomIdElement: "tache_INFINITY_FLOORS", idElement: "#tache_INFINITY_FLOORS", saisie: false }
]

// FR: les différentes sections
const idSectionProjet = [
    { nomIdSection: "a_faire", idSection: "#a_faire", nbrTache: 0 },
    { nomIdSection: "en_cours", idSection: "#en_cours", nbrTache: 0 },
    { nomIdSection: "fini", idSection: "#fini", nbrTache: 0 }
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
var xTache

// FR: déplacement du bloc de tâche
idElementBlocTacheProjet.forEach(({ nomIdElement, idElement, saisie }) => {
    let element = document.querySelector(idElement);

    // FR: si l'élément tache est pressé
    element.addEventListener("mousedown", function () {
        saisie = true;
        element.style.transition = "box-shadow 0.1s linear";
    });

    // FR: si pression souris levé
    element.addEventListener("click", function (event) {
        idSectionProjet.forEach(({ nomIdSection, idSection }) => {

            element.style.transition = "all 0.1s ease-in-out";

            // FR: récupère la position de la section
            const elementSection = document.querySelector(idSection);
            positionSection = elementSection.getBoundingClientRect();
            mouseX = event.clientX;
            mouseY = event.clientY;

            // FR: si souris dans la section
            if (mouseX > positionSection.left && mouseY > positionSection.top && mouseX < (positionSection.left + positionSection.width) && mouseY < (positionSection.top + positionSection.height)) {


                // FR: recherche le nombre de tâche dans chaque 
                idSectionProjet.forEach(({ idSection }) => {
                    const maDiv = document.querySelector(idSection);
                    const sections = maDiv.querySelectorAll(".bloc_projet");
                    xTache = sections.length;
                    console.log(xTache)
                });

                // FR: Stocker les informations de la tâche dans localStorage
                const tacheInfo = {
                    id: nomIdElement,
                    section: nomIdSection
                };
                localStorage.setItem(nomIdElement, JSON.stringify(tacheInfo));

                const elementTache = document.querySelector(idElement);
                positionTache = elementTache.getBoundingClientRect();
                Tachetop = (positionTache.top) - (positionSection.top)
                x = ((positionTache.left) - (positionSection.left)) - ((positionTache.width) * 0.025)
                y = y - ((positionTache.height * (xTache)) + ((positionTache.width) * 0.025))
                console.log(xTache)

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

// FR: restaurer la position des tâches enregistrées dans localStorage
idElementBlocTacheProjet.forEach(({ nomIdElement }) => {
    const tacheInfo = JSON.parse(localStorage.getItem(nomIdElement));
    if (tacheInfo) {
        const element = document.getElementById(nomIdElement);
        const section = document.getElementById(tacheInfo.section);
        section.appendChild(element);
    }
});

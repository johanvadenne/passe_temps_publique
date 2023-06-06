// ce code me permet d'aligner de élément

// récupère la position de l'élément
function elementPosition(a) {
    var b = a.getBoundingClientRect();
    return {
        clientX: a.offsetLeft,
        clientY: a.offsetTop,
        viewportX: (b.x || b.left),
        viewportY: (b.y || b.top)
    }
}

function repositionementElement() {

    // récupère l'élément "id = eleve_saisie"
    var mon_element = document.getElementById('premierElement');

    // je récupère sa position
    var positions = elementPosition(mon_element);

    // affiche dans la console
    console.log({
        "Position horizontale dans la fenêtre": positions.clientX,
        "Position verticale dans la fenêtre": positions.clientY,
        "Position horizontale dans le document": positions.viewportX,
        "Position verticale dans le document": positions.viewportY

    });

    // récupère l'élément "classe = selection"
    var selectElement = document.querySelector('.selection');

    // je position l'élément
    selectElement.style.left = (positions.viewportX - 300) + 'px';
    selectElement.style.top = positions.viewportY + 'px';

}

// fonction qui ce déclenche à la fin du chargement de la page
window.addEventListener('load', function () {

    repositionementElement();
});


// fonction qui ce déclenche à chaque redimentionement de l'écran
window.addEventListener("resize", function () {

    repositionementElement();
});

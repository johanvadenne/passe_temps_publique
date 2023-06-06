// FR: élément lien
// EN: element link
const elementLienId = [
    {idLienBouton:"#lien_html", idImage:"#html"}, 
    {idLienBouton:"#lien_css", idImage:"#css"},
    {idLienBouton:"#lien_js", idImage:"#js"},
    {idLienBouton:"#lien_bloc1", idImage:"#bloc1"},
    {idLienBouton:"#lien_bloc2", idImage:"#bloc2"},
    {idLienBouton:"#lien_bloc3", idImage:"#bloc3"},
    {idLienBouton:"#lien_3d", idImage:"#troisd"},
    {idLienBouton:"#lien_web", idImage:"#web"},
    {idLienBouton:"#lien_design", idImage:"#design"},
    {idLienBouton:"#lien_mon_stie", idImage:"#mon_stie"},
    {idLienBouton:"#lien_frelots", idImage:"#frelots"},
    {idLienBouton:"#lien_infinity_floors", idImage:"#floors"}
]

// FR: élément fond
// EN: background element
const elementIdFond = [
    {idElement:"#etude", elementFond:"#fond_etude"},
    {idElement:"#language", elementFond:"#fond_language"},
    {idElement:"#programme", elementFond:"#fond_programme"},
    {idElement:"#projet", elementFond:"#fond_projet"}
]

let position = 0;

// FR: pour chaque élément lien
// EN: for each link element
elementLienId.forEach(({idLienBouton, idImage}) => {
    const lien = document.querySelector(idLienBouton)
    
    // FR: si on le survole affiche l'image
    // EN: if you hover it displays the image
    lien.addEventListener("mouseover", function () {
        const image = document.querySelector(idImage)
        image.style.opacity = "1"
        image.style.visibility = "visible"
        image.style.transform = "translateX(20px)"

    });

    
    // FR: si on ne le survole plus retire l'image
    // EN: if you don't hover over it anymore remove the image
    lien.addEventListener("mouseout", function () {
        const image = document.querySelector(idImage)
        image.style.opacity = "0"
        image.style.transform = "translateX(-20px)"
    });
});

// FR: pour chaque élément du menu
// EN: for each menu item
elementIdFond.forEach(({idElement, elementFond}) => {
    const element = document.querySelector(idElement)
    
    // FR: if you hover over it, display the background
    // EN: si on le survole affiche le fond écran
    element.addEventListener("mouseover", function () {
        const fond = document.querySelector(elementFond)
        fond.style.opacity = "1"
    });

    // FR: si on ne le survole plus retire le fond écran
    // EN: if you don't hover over it anymore, remove the background
    element.addEventListener("mouseout", function () {
        const fond = document.querySelector(elementFond)
        fond.style.opacity = "0"
    });
});
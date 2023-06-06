  // fr: initialisations variables
  // en: variable initializations

  var sequencesOfButtons = [];
  var time = 0;
  var presse = false
  var numSuite = 0;
  var idcheck = 0;
  var win = true
  var finishLap = false
  var play = true
  var bestScore = 0
  var textMenu = ""

// fr: boutons
// en: buttons
const buttons = [
    { id: "#jaune", color: "rgb(182, 182, 0)", defaultColor: "yellow" },
    { id: "#bleu", color: "rgb(0, 0, 209)", defaultColor: "blue" },
    { id: "#rouge", color: "rgb(202, 0, 0)", defaultColor: "red" },
    { id: "#vert", color: "rgb(0, 100, 0)", defaultColor: "green" }
];

// fr: allume ou éteints le bouton
// en: turns on or off the button
function onOff(id, color) {
    let button = document.querySelector(id);
    button.style.backgroundColor = color
}

// fr: fais une animation de tourbillon
// en: make a swirl animation
function animationwhirlwind(typeColor, callBack = ""){
    let ind = 0;
    let interval = setInterval(function() {
        id = buttons[ind].id;
        color = buttons[ind][typeColor];
        onOff(id, color)
        ind++;
        if (ind >= buttons.length) {
            clearInterval(interval)
            callBack();
        }
    }, 100)
}

// fr: fait un flash
// en: makes a flash
function flashing(callBack = ""){
    buttons.forEach(({id, color, defaultColor}) => {
        onOff(id, color)
        setTimeout(() => {onOff(id, defaultColor);}, 200);
    });
    setTimeout(() => {callBack();}, 1000);
}

// fr: affiche la suite
// en: displays the suite
function displaysSuite() {
    
    // fr: initialize variables
    // en: variable initializations
    let i = 0;
    let numSelectButton = 0;
    
    // fr: prend un nombre aléatoire entre 0 et 3
    // en: takes a random number between 0 and 3
    var x = Math.floor(Math.random() * 4);
    
    // fr: ajoute le nombre au tableau
    // en: add the number to the table
    sequencesOfButtons.push(x);
    
    // fr: toute les 0.5 sencondes affiche un boutons
    // en: every 0.5 seconds displays a button
    var interval = setInterval(function() {
        
        // fr: récupère le numéro lié au bouton
        // en: retrieves the number linked to the button
        numSelectButton = sequencesOfButtons[i];
        
        // fr: récupère l'id, la couleur, et la couleur par défault du bouton
        // en: retrieves the id, the color, and the default color of the button
        id = buttons[numSelectButton].id;
        color = buttons[numSelectButton].color;
        defaultColor = buttons[numSelectButton].defaultColor;
        
        // fr: éteint le bouton 
        // en: turn off the button
        onOff(id, color)
        
        // fr: allume le bouton après 0.5 seconde
        // en: turns on the button after 0.5 seconds
        setTimeout(() => {
            onOff(id, defaultColor)
        }, 250);
        i++;
        
        // fr: si la séquence est terminé arrèté la boucle
        // en: if the sequence is finished stop the loop
        if (i >= sequencesOfButtons.length) {
            clearInterval(interval);
            player();
        }
    }, 500)
}

// fr: vérifie si la suite du joueur est bon
// en: checks if the player's suite is good
function check(id) {

    // fr: récupère l'id de la séquence
    // en: retrieves the id of the sequence
    idcheck = buttons[sequencesOfButtons[numSuite]].id;

    // fr: si ce son les même
    // en: if they are the same
    if (id === idcheck) {
        numSuite++;
        
        // fr: si la séquance est terminer
        // en: if the sequence is completed
        if (numSuite >= sequencesOfButtons.length) {
            numSuite = 0;
            finishLap = true
            win = true
            return null;
        }
    }
    
    // fr: sinon terminé
    // en: else finish
    else {
        finishLap = true;
        win = false;
    }
    return null;
}

// fr: supprime les éventement d'écoute
// en: removes listening events
function removeButtonEventListeners() {
    buttons.forEach(({ id }) => {
      const bouton = document.querySelector(id)
      const boutonClone = bouton.cloneNode(true);
      bouton.parentNode.replaceChild(boutonClone, bouton);
    });
  }

// fr: active les éventements d'écoute lorsque le joueur joue
// en: activates the listening events when the player plays
function player() {
    
    // fr: pour chaque boutons de la table
    // en: for each button of the table
    buttons.forEach(({id, color, defaultColor}) => {
        const bouton = document.querySelector(id)

        // fr: si il appuie sur un bouton "presse = vrai" et change la couleur
        // fr: if he presses a button "press = true" and changes the color
        bouton.addEventListener("mousedown", function () {
            onOff(id, color);
            presse = true;
        });

        // fr: si il quitte l'élément "presse = false" et change la couleur
        // en: if it leaves the element "press = false" and changes the color
        bouton.addEventListener("mouseout", function () {
            onOff(id, defaultColor);
            presse = false;
        });

        // fr: si il lève sa souris change la couleur
        // en: if it raises its mouse changes the color
        bouton.addEventListener("mouseup", function () {
            onOff(id, defaultColor);

            if (presse) {
                presse = false;

                // fr: vérifie si le joueur appuie sur les bons boutons
                // en: checks if the player presses the right buttons
                check(id);
                if (win && finishLap) {
                    finishLap = playerPlay = false;
                    removeButtonEventListeners();
                    displaysSuite();
                }
                else if (!win) {
                    finishLap = lapPlayer = false;
                    removeButtonEventListeners();
                    lose();
                    return;
                }
            }
        });
    });
    
}

// fr: lance le jeu
// en: start the game
function game(){
    numSuite = 0;
    sequencesOfButtons = []

    button = document.querySelector("#menu")
    button.style.display = "none";
    animationwhirlwind("color", function() {
        animationwhirlwind("defaultColor", function() {
            flashing(function(){
                displaysSuite()
            });
        });
    });
}

// fr: affiche le menu principale
// en: displays the main menu
function lose() {
    if (bestScore < sequencesOfButtons.length-1) {
        bestScore = sequencesOfButtons.length-1
    }
    textMenu="Meilleurs recors\n"+(bestScore)
    elementText = document.getElementById("menuText")
    elementText.innerHTML = textMenu
    button = document.querySelector("#menu")
    button.style.display = "flex";
}
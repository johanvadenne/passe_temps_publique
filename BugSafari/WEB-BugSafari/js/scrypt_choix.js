/*
Connection a la BDD
*/
// Utilisez une bibliothèque comme jQuery ou utilisez l'API Fetch si elle est disponible
// dans votre environnement pour effectuer une requête AJAX.

// Exemple d'utilisation de l'API Fetch pour effectuer une requête GET

fetch('http://172.16.197.254:8080/api/Ticket')
    .then(response => {
        if (!response.ok) {
            throw new Error(`Erreur HTTP! Statut : ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        // Les données de la base de données sont disponibles dans la variable 'data'
        console.log(data);

        // Appel de la fonction pour remplir le tableau avec les données
        fillTable(data);
    })
    .catch(error => {
        console.error('Erreur lors de la récupération des données:', error);
    });

function fillTable(demandeChangement) {
    let addcolonne = '';

    for (let i = 0; i < demandeChangement.length; i++) {
        const changement = demandeChangement[i];

        // Création de la structure pour le tableau avec des boutons
        addcolonne += `<tr>`;
        addcolonne += `<td>${changement.IdCompteUtilisateur}</td>`;
        addcolonne += `<td>${changement.IdTicket}</td>`;
        addcolonne += `<td><button data-id="${changement.IdTicket}" onclick="accepterChangement(this)">Accepter</button></td>`;
        addcolonne += `<td><button data-id="${changement.IdTicket}" onclick="refuserChangement(this)">Refuser</button></td>`;
        addcolonne += `</tr>`;
    }

    // Ajout à la page HTML
    document.getElementById("tableau").innerHTML += addcolonne;
}

// Fonction pour gérer l'acceptation d'un changement
function accepterChangement(button) {
    // Récupérer l'ID de la ligne à accepter à partir de l'attribut data-id du bouton
    var id = button.getAttribute('data-id');

    // Envoyer une requête AJAX pour supprimer la ligne avec l'ID spécifié
    fetch(`../php/accepter.php?id=${id}`)
        .then(response => response.json())
        .then(data => {
            console.log(`Changement accepté avec succès.`, data);
            // Recharger les données après avoir accepté le changement
            location.reload();
        })
        .catch(error => {
            console.error('Erreur lors de l\'acceptation du changement:', error);
        });
}

// Fonction pour gérer le refus d'un changement
function refuserChangement(button) {
    // Récupérer l'ID de la ligne à refuser à partir de l'attribut data-id du bouton
    var id = button.getAttribute('data-id');

    // Envoyer une requête AJAX pour supprimer la ligne avec l'ID spécifié
    fetch(`../php/refuser.php?id=${id}`)

    .catch(error => {
        console.error('Erreur lors du refus du changement:', error);
    });
}
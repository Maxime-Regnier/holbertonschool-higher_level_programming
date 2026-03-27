fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
.then(response => response.json())
.then(data => {
const characterName = data.name;
const characterDiv = document.querySelector('#character');
characterDiv.textContent = characterName;
})
.catch(error => {
    console.error('Erreur lors de la récupération des données:', error);
    document.querySelector('#character').textContent = 'Erreur: impossible de charger le personnage';
});
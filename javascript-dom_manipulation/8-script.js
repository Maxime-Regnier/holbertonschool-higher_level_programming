document.addEventListener('DOMContentLoaded', function() {
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
        document.querySelector('#hello').textContent = data.hello;
    })
    .catch(error => {
        console.error('Erreur:', error);
        document.querySelector('#hello').textContent = 'Erreur: impossible de charger la traduction';
    });
});
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(response => response.json())
.then(data => {
    const films = data.results;
    const listMovies = document.querySelector('#list_movies');
    films.forEach(film => {
        const li = document.createElement('li');
        li.textContent = film.title;
        listMovies.appendChild(li);
    });
})
.catch(error => {
    console.error('Erreur:', error);
    document.querySelector('#list_movies').textContent = 'Erreur: impossible de charger les films';
});
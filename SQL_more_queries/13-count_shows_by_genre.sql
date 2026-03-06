-- Script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT genres.name as genre, COUNT(tv_shows.id) as number_of_shows
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY genres.id, genres.name
HAVING COUNT(tv_shows.id) > 0
ORDER BY number_of_shows DESC;
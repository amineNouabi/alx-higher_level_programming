-- Count the number of shows for each genre. --
SELECT tv_genres.name as genre, COUNT(tv_genres.id) as number_of_shows
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.id
ORDER BY number_of_shows DESC;

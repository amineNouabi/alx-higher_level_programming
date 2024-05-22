-- Show all the shows, and their genres, ordered by the show's title and the genre's name. --
SELECT tv_shows.title AS title,
	   tv_genres.name AS name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY title ASC, name ASC;

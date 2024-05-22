-- Show the title and genre_id of all TV shows, ordered by title and genre_id. --
SELECT title, genre_id FROM tv_shows RIGHT JOIN tv_show_genres ON id = show_id ORDER BY title ASC, genre_id ASC;

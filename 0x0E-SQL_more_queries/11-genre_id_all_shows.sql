-- Show all the shows with their genre_id, ordered by title and genre_id. --
SELECT title, genre_id FROM tv_shows LEFT JOIN tv_show_genres ON id = show_id ORDER BY title ASC, genre_id ASC;

-- Show all the shows with their genre_id equals NULL --
SELECT title, genre_id FROM tv_shows LEFT JOIN tv_show_genres ON id = show_id WHERE genre_id IS NULL ORDER BY title ASC, genre_id ASC;

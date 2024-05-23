-- Show the title of the TV show and the rating that it has received, ordered by rating in descending order. --
SELECT tv_shows.title AS title,
	   SUM(tv_show_ratings.rate) AS rating
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;

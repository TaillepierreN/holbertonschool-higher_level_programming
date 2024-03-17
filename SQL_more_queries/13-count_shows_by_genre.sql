-- List all genres from hbtn_0d_tvshows and display the number of shows liked to each
-- Display <TV Show genre> - <Number of shows linked to this genre>
SELECT
	tv_genres.name AS genre,
	COUNT(tv_show_genres.genre_id) AS number_of_shows
FROM
	tv_show_genres
	JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY
	tv_show_genres.genre_id
ORDER BY
	number_of_shows DESC,
	tv_genres.id ASC

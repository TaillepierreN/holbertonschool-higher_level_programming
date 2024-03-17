-- List all shows in hbtn_0d_tvshows without a genre
-- display: tw_shows.title - tv_show_genres.genre_id
use hbtn_0d_tvshows;

SELECT
	tv_shows.title,
	tv_show_genres.genre_id
FROM
	hbtn_0d_tvshows.tv_shows
	LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE
	tv_show_genres.genre_id IS NULL
ORDER BY
	tv_shows.title

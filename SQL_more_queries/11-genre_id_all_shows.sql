-- list all shows in tvshows
-- display: tv_shows.title - tv_show_genres.genre_id/NULL
use hbtn_0d_tvshows;
SELECT
	tv_shows.title,
	tv_show_genres.genre_id
FROM
	hbtn_0d_tvshows.tv_shows
	LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY
	tv_shows.title,
	tv_show_genres.genre_id
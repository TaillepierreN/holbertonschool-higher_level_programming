-- List the number of records with the same score in second_table
-- only displaying the score,the number of records of this score with label number
SELECT
	score,
	COUNT(*) AS number
FROM
	second_table
GROUP BY
	score
ORDER BY
	score DESC

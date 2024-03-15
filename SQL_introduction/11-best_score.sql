-- List all records with a score higher than 10 in second_table,only displaying both score(top first) and name
SELECT
	score,
	name
FROM
	second_table
WHERE
	score >= 10
ORDER BY
	score DESC

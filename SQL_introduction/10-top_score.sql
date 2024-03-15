-- List all records of second_table,only displaying both score(top first) and name
SELECT
	score,
	name
FROM
	second_table
ORDER BY
	score DESC

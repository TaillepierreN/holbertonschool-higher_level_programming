-- List all records of the second_table,skipping the rows without a name, displaying score(descending order) and name
SELECT
	score,
	name
FROM
	second_table
WHERE
	name IS NOT NULL
ORDER BY
	score DESC

-- List all the cities in California that can be found in hbtn_0d_usa
SELECT
	*
FROM
	hbtn_0d_usa.cities
WHERE
	state_id = (
		SELECT
			id
		FROM
			hbtn_0d_usa.states
		WHERE
			name = 'California'
	)

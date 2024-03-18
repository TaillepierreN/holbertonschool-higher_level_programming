-- List all the cities in California that can be found in hbtn_0d_usa
SELECT id, name
FROM cities
WHERE
    cities.state_id = (
        SELECT id
        FROM states
        WHERE
            name = 'California'
    )
ORDER BY cities.id ASC

-- List all cities contained in hbtn_0d_usa
-- display: cities.id(ascending) - cities.name - states.name
SELECT
	cities.id,
	cities.name,
	states.name
FROM
	hbtn_0d_usa.cities
	JOIN states ON cities.state_id = states.id

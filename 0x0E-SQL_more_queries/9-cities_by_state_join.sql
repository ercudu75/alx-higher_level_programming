-- lists all cities contained in the database
SELECT C.id, C.name, S.name
FROM cities C, states S
WHERE S.id = C.state_id
ORDER BY C.id;

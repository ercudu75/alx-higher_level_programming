-- lists all the cities of California
SELECT S.id, C.name
FROM states S, cities C
WHERE S.id = C.id
ORDER BY S.id;

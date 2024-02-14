-- lists all the cities of California
SELECT C.id, C.name
FROM states S, cities C
WHERE S.id = C.id
AND S.name = "California"
ORDER BY C.id;

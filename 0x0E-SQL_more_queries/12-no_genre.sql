-- lists of all shows in a database
SELECT T.title, TG.genre_id
FROM tv_show_genres TG RIGHT JOIN tv_shows T
ON TG.show_id = T.id
WHERE TG.genre_id IS NULL
ORDER BY T.title, TG.genre_id;

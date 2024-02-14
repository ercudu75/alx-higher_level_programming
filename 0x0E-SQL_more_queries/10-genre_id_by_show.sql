-- lists of all shows in a database
SELECT T.title, TG.genre_id
FROM tv_show_genres TG, tv_shows T
WHERE TG.show_id = T.id
ORDER BY T.title, TG.genre_id;

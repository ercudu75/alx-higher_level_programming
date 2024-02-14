-- displays lists all shows, and
-- all genres linked to that show,
SELECT S.title AS title, G.name AS name
FROM tv_shows S LEFT JOIN tv_show_genres TG
ON S.id = TG.show_id
LEFT JOIN tv_genres G
ON TG.genre_id = G.id
ORDER BY title, name;

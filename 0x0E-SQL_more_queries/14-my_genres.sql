-- script that lists all genre and
-- displays the number of shows linked to each
SELECT G.name AS name
FROM tv_genres G, tv_show_genres TG, tv_shows S
WHERE G.id = TG.genre_id
AND TG.show_id = S.id
AND S.title = "Dexter"
ORDER BY name;

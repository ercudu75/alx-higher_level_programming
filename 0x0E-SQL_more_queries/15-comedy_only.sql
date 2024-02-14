-- script that lists all genre and
-- displays the number of shows linked to each
SELECT S.title AS title
FROM tv_genres G, tv_show_genres TG, tv_shows S
WHERE G.id = TG.genre_id
AND TG.show_id = S.id
AND G.name = "Comedy"
ORDER BY title;

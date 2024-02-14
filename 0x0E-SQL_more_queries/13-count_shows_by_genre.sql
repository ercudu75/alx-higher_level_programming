-- script that lists all genre and
-- displays the number of shows linked to each
SELECT G.name, COUNT(TG.genre_id) AS number_of_shows
FROM tv_genres G, tv_show_genres TG
WHERE G.id = TG.genre_id
GROUP BY G.name
ORDER BY number_of_shows DESC;

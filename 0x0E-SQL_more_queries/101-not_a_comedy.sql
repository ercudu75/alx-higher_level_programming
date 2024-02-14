-- lists all shows without the genre
SELECT S.title AS title
FROM tv_shows S
WHERE S.id NOT IN (
	SELECT TG.show_id
	FROM tv_show_genres TG INNER JOIN tv_genres G
	ON TG.genre_id = G.id
	WHERE G.name = "Comedy"
)
ORDER BY title;

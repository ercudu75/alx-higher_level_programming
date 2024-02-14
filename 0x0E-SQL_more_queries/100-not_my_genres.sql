-- to list all genres not linked to the show Dexter
SELECT G.name as name
FROM tv_genres G
WHERE G.id NOT IN (
	SELECT G.id
	FROM tv_genres G INNER JOIN tv_show_genres TG
	ON G.id = TG.genre_id
	INNER JOIN tv_shows S
	ON TG.show_id = S.id
	WHERE S.title = "Dexter"
)
ORDER BY name;

-- lists all shows by their rating
SELECT S.title AS title, SUM(TR.rate) AS rating
FROM tv_shows S LEFT JOIN tv_show_ratings TR
ON TR.show_id = S.id
GROUP BY title
ORDER BY rating DESC;

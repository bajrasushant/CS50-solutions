SELECT titles FROM movies
WHERE id in (SELECT movie_id FROM stars
WHERE person_id IN (SELECT ))
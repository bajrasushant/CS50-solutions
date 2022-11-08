SELECT * FROM movies
WHERE id IN
(SELECT movie_id FROM stars
WHERE person_id IN (SELECT id FROM people WHERE name = "Johnny Depp")) AS a
SELECT titles FROM A
WHERE id IN
(SELECT movie_id FROM stars
WHERE person_id IN (SELECT id FROM people WHERE name = "Helena Bonham Carter"));
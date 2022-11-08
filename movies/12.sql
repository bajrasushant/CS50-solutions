-- SELECT title FROM movies
-- WHERE id in (SELECT movie_id FROM stars
-- WHERE person_id IN (SELECT id FROM people WHERE name = "Johnny Depp"))
-- INTERSECT SELECT title FROM movies
-- WHERE id in (SELECT movie_id FROM stars
-- WHERE person_id IN (SELECT id FROM people WHERE name = "Helena Bonham Carter"));

SELECT title FROM movies, stars, people
WHERE people.name = "Johnny Depp"
AND stars.person_id = people.id
AND movies.id = stars.movie_id
INTERSECT
SELECT title FROM movies, stars, people
WHERE people.name = "Helena Bonham Carter"
AND stars.person_id = people.id
AND movies.id = stars.movie_id;
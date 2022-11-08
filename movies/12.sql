SELECT title FROM movies, stars, people
WHERE movies.id =
(SELECT movie_id FROM stars WHERE person_id IN (SELECT id FROM people WHERE name = "Johnny Depp"));
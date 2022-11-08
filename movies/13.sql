-- SELECT DISTINCT(name) from people, movies, stars
-- WHERE movies.title =
-- (SELECT title FROM movies, people, stars
-- WHERE people.name = "Kevin Bacon"
-- AND stars.person_id = people.id
-- AND movies.id = stars.movie_id)
-- AND stars.movie_id = movies.id
-- AND people.id = stars.person_id;
SELECT DISTINCT(name) FROM people, movies
WHERE people.id IN (SELECT id FROM movies) (SELECT title FROM people, movies, stars
WHERE people.name = "Kevin Bacon"
AND people.birth = 1958
AND stars.person_id = people.id
AND movies.id = stars.movie_id);
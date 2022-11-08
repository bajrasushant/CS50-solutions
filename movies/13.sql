SELECT DISTINCT(name) from people, movies, stars
WHERE people.id = stars.person_id
AND stars.movie_id = movies.id
AND movies.title IN
(SELECT title FROM movies, people, stars
WHERE movies.id = stars.movie_id
AND stars.person_id = people.id
AND people.name = "Kevin Bacon")
INTERSECT
SELECT name from people
WHERE name <> "Kevin Bacon"
AND birth <> 1958
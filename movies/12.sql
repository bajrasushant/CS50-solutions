SELECT title FROM movies, stars, people
WHERE movies.id =
(SELECT id FROM movies)
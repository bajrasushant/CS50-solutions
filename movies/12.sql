SELECT title FROM movies, stars, people
WHERE movies.id = 
(SELECT id FROM movies, stars
WHERE stars.movie_id IN
(SELECT movie_id FROM stars
WHERE person_id IN (SELECT id FROM people WHERE name = "Johnny Depp")) AND people.name = "Helena Bonham Carter";
SELECT DISTINCT(name) FROM people, movies, stars
WHERE movies.year = 2004
AND stars.movie_id = movies.id
AND people.id = stars.person_id
ORDER BY people.birth;
SELECT title FROM movies, people, stars
WHERE people.name = "Kevin Bacon"
AND stars.person_id = people.id
AND movies.id = stars.movies_id;
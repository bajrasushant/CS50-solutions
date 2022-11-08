SELECT title FROM movies, ratings, people, stars
WHERE people.name = "Chadwick Boseman"
AND stars.person_id = people.id
AND movies.id = stars.movie_id
ORDER BY rating DESC
LIMIT 5;
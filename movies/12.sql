SELECT title FROM movies, stars, people
WHERE movies.id = stars.movie_id
AND stars.person_id = people.id
AND people.id = ("Johnny Depp", "Helena Bonham Carter")
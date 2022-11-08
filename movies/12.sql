SELECT title FROM movies, stars, people
WHERE movies.id = stars.movie_id
AND people.id = ("Johnny Depp", "Helena Bonham Carter")
AND stars.person_id = people.id;
SELECT title FROM movies, stars, people
AND people.id = ("Johnny Depp", "Helena Bonham Carter")
AND stars.person_id = people.id
WHERE movies.id = stars.movie_id
GROUP BY movies.title
HAVING COUNT(movies.title) = 2;
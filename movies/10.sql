SELECT DISTINCT(name) FROM people, ratings, directors
Where ratings.rating >= 9.0
AND directors.movie_id = ratings.movie_id
AND people.id = directors.person_id;
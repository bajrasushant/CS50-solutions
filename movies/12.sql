SELECT title FROM movies, people, stars
WHERE people.name = "Johnny Depp", people.name = "Helena Bonham Carter"
AND stars.person_id = people.id
AND
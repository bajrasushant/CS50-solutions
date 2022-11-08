-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports WHERE street = "Humphrey Street" AND month = 7 AND day = 28;
-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
--Interviews were conducted today with three witnesses who were present at the time
-- each of their interview transcripts mentions the bakery.

SELECT * FROM interviews WHERE month = 7 AND day = 28;
--Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
--Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money. (Eugene)
--As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
--I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.

SELECT * FROM bakery_security_logs WHERE month = 7 AND day = 28;
--13FNH73, 5P2BI95, 94KL13X, 6P58WS2, 4328GD8, G412CB7, L93JTIZ, 322W7JE, 0NTHK55 5 vehicles out in 10 minutes

SELECT * FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 60;
--record less than 60 second

SELECT name FROM people
WHERE phone_number IN (SELECT caller FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 60);
--callers(Kenny   || Sofia   || Benista || Taylor  || Diana   || Kelsey  || Bruce   || Carina

SELECT name FROM people
WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE month = 7 AND day = 28 AND duration < 60);
--receiver James  || Larry   || Anna    || Jack    || Melissa || Jacqueline|| Philip|| Robin|| Doris

SELECT * FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw";
-- people withdrawing money

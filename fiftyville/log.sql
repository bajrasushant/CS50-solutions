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

SELECT name FROM people WHERE id IN (SELECT person_id FROM bank_accounts WHERE account_number in (SELECT account_number FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw"));
--person id (kenny, iman, benista, taylor, brooke, luca, diana, bruce)

SELECT name FROM people
WHERE phone_number IN
    (SELECT caller FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT name FROM people
WHERE id IN
    (SELECT person_id FROM bank_accounts
        WHERE account_number in
            (SELECT account_number FROM atm_transactions
                WHERE month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw"));
--common people, calling and withdrawing the same day(benista, bruce, diana, kenny, taylor)

-- SELECT name FROM people
-- WHERE phone_number IN
--     (SELECT receiver FROM phone_calls
--     WHERE month = 7 AND day = 28 AND duration < 60)
-- INTERSECT
-- SELECT name FROM people
-- WHERE id IN
--     (SELECT person_id FROM bank_accounts
--         WHERE account_number in
--             (SELECT account_number FROM atm_transactions
--                 WHERE month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw"));
--                 --0 common people

SELECT license_plate FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour = 10;
--license plate checking

SELECT name FROM people WHERE license_plate IN
    (SELECT license_plate FROM bakery_security_logs
    WHERE month = 7 AND day = 28 AND hour = 10)
INTERSECT
SELECT name FROM people
WHERE phone_number IN
    (SELECT caller FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT name FROM people
WHERE id IN
    (SELECT person_id FROM bank_accounts
        WHERE account_number in
            (SELECT account_number FROM atm_transactions
                WHERE month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw"));
-- bruce diana taylor leaving the bakery, at the atm withdrawing and calling for less than 60s

SELECT full_name, city FROM airports WHERE id IN(SELECT destination_airport_id FROM flights WHERE origin_airport_id = 8 AND month = 7 AND day = 29);
--chicago, new york, boston, tokyo, sanfrancisco

SELECT id, destination_airport_id FROM flights WHERE origin_airport_id = 8 AND month = 7 AND day = 29;
-- 18 23 36 43 53

SELECT name FROM people WHERE passport_number IN
    (SELECT passport_number FROM passengers
        WHERE flight_id IN
            (SELECT id FROM flights
                WHERE origin_airport_id = 8 AND month = 7 AND day = 29))
INTERSECT
SELECT name FROM people WHERE license_plate IN
    (SELECT license_plate FROM bakery_security_logs
        WHERE month = 7 AND day = 28 AND hour = 10)
INTERSECT
SELECT name FROM people
WHERE phone_number IN
    (SELECT caller FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT name FROM people
WHERE id IN
    (SELECT person_id FROM bank_accounts
        WHERE account_number in
            (SELECT account_number FROM atm_transactions
                WHERE month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw"));
-- bruce diana taylor


SELECT name FROM people
WHERE phone_number IN
    (SELECT receiver FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration < 60)
INTERSECT
    SELECT name FROM people WHERE passport_number IN
    (SELECT passport_number FROM passengers
        WHERE flight_id IN
            (SELECT id FROM flights
                WHERE origin_airport_id = 8 AND month = 7 AND day = 29));
    -- doris larry melissa receiving the phone and in flight

SELECT flight_id, seat, passport_number FROM passengers WHERE passport_number IN
(SELECT passport_number FROM people
WHERE phone_number IN
    (SELECT receiver FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT passport_number FROM passengers
WHERE flight_id IN
        (SELECT id FROM flights
        WHERE origin_airport_id = 8 AND month = 7 AND day = 29));
        -- (2B 6A 7B 5B 4D 8C) repeating passport number, distinct 2A 7214083635

SELECT flight_id, seat, passport_number from passengers WHERE passport_number IN(
SELECT passport_number FROM passengers
        WHERE flight_id IN
            (SELECT id FROM flights
                WHERE origin_airport_id = 8 AND month = 7 AND day = 29)
INTERSECT
SELECT passport_number FROM people WHERE license_plate IN
    (SELECT license_plate FROM bakery_security_logs
        WHERE month = 7 AND day = 28 AND hour = 10)
INTERSECT
SELECT passport_number FROM people
WHERE phone_number IN
    (SELECT caller FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT passport_number FROM people
WHERE id IN
    (SELECT person_id FROM bank_accounts
        WHERE account_number in
            (SELECT account_number FROM atm_transactions
                WHERE month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw")));
                --checking from common flight id


SELECT flight_id FROM passengers WHERE passport_number IN
(SELECT passport_number FROM people
WHERE phone_number IN
    (SELECT receiver FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT passport_number FROM passengers
WHERE flight_id IN
        (SELECT id FROM flights
        WHERE origin_airport_id = 8 AND month = 7 AND day = 29))
INTERSECT
SELECT flight_id from passengers WHERE passport_number IN(
SELECT passport_number FROM passengers
        WHERE flight_id IN
            (SELECT id FROM flights
                WHERE origin_airport_id = 8 AND month = 7 AND day = 29)
INTERSECT
SELECT passport_number FROM people WHERE license_plate IN
    (SELECT license_plate FROM bakery_security_logs
        WHERE month = 7 AND day = 28 AND hour = 10)
INTERSECT
SELECT passport_number FROM people
WHERE phone_number IN
    (SELECT caller FROM phone_calls
    WHERE month = 7 AND day = 28 AND duration < 60)
INTERSECT
SELECT passport_number FROM people
WHERE id IN
    (SELECT person_id FROM bank_accounts
        WHERE account_number in
            (SELECT account_number FROM atm_transactions
                WHERE month = 7 AND day = 28 AND atm_location = "Leggett Street" AND transaction_type = "withdraw")));
                -- flight 36

SELECT origin_airport_id, destination_airport_id from flights WHERE id = 36 AND day = 29 AND month = 7;
-- DESTINATION 4(NY)

-- flight 36 has two of the 3 suspects bruce, taylor

SELECT receiver FROM phone_calls WHERE caller = "(367) 555-5533" AND duration < 60 AND month = 7 AND day = 28; --checking for receiver (helper of bruce)

SELECT * FROM people WHERE phone_number = "(375) 555-8161"; -- robin no passport number##

SELECT receiver FROM phone_calls WHERE caller = "(286) 555-6063" AND duration < 60 AND month = 7 AND day = 28; --cheking for receiver phone (helper of taylor)

SELECT * FROM people WHERE phone_number = "(676) 555-6554"; --james

SELECT flight_id FROM passengers WHERE passport_number =2438825627; --checking if james in flight 36 noooo

-- so the theives might be bruce and robin flying to newyork city
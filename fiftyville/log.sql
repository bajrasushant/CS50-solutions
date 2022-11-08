-- Keep a log of any SQL queries you execute as you solve the mystery.
SELECT * FROM crime_scene_reports WHERE street = "Humphrey Street" AND month = 7 AND day = 28;
-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
--Interviews were conducted today with three witnesses who were present at the time
-- each of their interview transcripts mentions the bakery.

SELECT * FROM interviews WHERE month = 7 AND day = 28;
--Sometime within ten minutes of the theft, I saw the thief get into a car in the bakery parking lot and drive away.
--Earlier this morning, before I arrived at Emma's bakery, I was walking by the ATM on Leggett Street and saw the thief there withdrawing some money.
--As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
--I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.

SELECT * FROM bakery WHERE month = 7 AND day = 28;
-- Keep a log of any SQL queries you execute as you solve the mystery.
-- the theft took place on july 28,2021 on Humphrey Street
SELECT * FROM crime_scene_reports; -- to check for crimes and details time
--theft at 10:15, 3 witness, bakery
SELECT * FROM bakery_security_logs; -- to check who came at 10:15
--at 10:14 13FNH73 entered(license plate)
SELECT * FROM PEOPLE WHERE license_plate = "13FNH73";--Sophia vehicle 342612721(passport)
--(027) 555-1068 (phone number)
SELECT * FROM interviews WHERE year = 2021 AND month = 7 AND day = 28;
--check footage after 10 mins car
--cashing atm on earlier morning
--earliest flight out of fiftyville the next day

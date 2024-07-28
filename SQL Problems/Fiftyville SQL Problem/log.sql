-- Keep a log of any SQL queries you execute as you solve the mystery.
--Answear By Fabian C.
-- Frist step (from Walkthrough)
SELECT description FROM crime_scene_reports WHERE month = 7 AND day = 28 AND street = 'Humphrey Street';
--Second Step
SELECT transcript FROM interviews WHERE day = 28 AND month = 7 AND transcript LIKE '%bakery%';
-- Third Step
SELECT * FROM bakery_security_logs WHERE day = 28 AND month = 7 AND hour = 10 AND minute BETWEEN 15 AND 25;
-- Fourth Step (names)
SELECT p.name from people p JOIN bakery_security_logs ON p.license_plate = bakery_security_logs.license_plate WHERE bakery_security_logs.day = 28 AND bakery_security_logs.month = 7 AND bakery_security_logs.hour = 10 AND bakery_security_logs.minute BETWEEN 15 AND 25;
-- Fifth Step
SELECT * FROM atm_transactions WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street';
-- Sixth Step (finding the depositer)
SELECT people.name FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id JOIN atm_transactions ON bank_accounts.account_number = atm_transactions.account_number WHERE month = 7 AND day = 28 AND atm_location = 'Leggett Street';
-- Seventh Step
SELECT caller FROM phone_calls WHERE month = 7 AND day = 28 AND duration <= 60;
-- Eight Step
SELECT people.name FROM people JOIN phone_calls ON people.phone_number = phone_calls.caller WHERE phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration <= 60;
-- Ninth Step
SELECT * FROM airports WHERE city = 'Fiftyville';
-- Tenth Step
SELECT * FROM flights WHERE origin_airport_id = 8 AND flights.month = 7 AND flights.day = 29;
-- Eleventh Step (WE FOUND BRUCE!)
SELECT people.name FROM people JOIN passengers ON people.passport_number = passengers.passport_number JOIN flights ON passengers.flight_id = flights.id JOIN airports ON flights.origin_airport_id = airports.id WHERE airports.city = 'Fiftyville' AND flights.month = 7 AND flights.day = 29 AND flights.hour = 8 AND flights.minute = 20;
-- Twelfth Step (He escaped to NYC)
SELECT airports.city FROM airports JOIN flights ON airports.id = flights.destination_airport_id WHERE flights.origin_airport_id = 8 AND flights.month = 7 AND flights.day = 29 AND flights.hour = 8 AND flights.minute = 20;
-- Thirteenth Step (Let's find the accomplice!)
SELECT phone_number FROM people WHERE name = 'Bruce';
-- Fourteenth Step (It's ROBIN!)
SELECT people.name FROM people JOIN phone_calls ON people.phone_number = phone_calls.receiver WHERE phone_calls.month = 7 AND phone_calls.day = 28 AND phone_calls.duration <= 60 AND phone_calls.caller = '(367) 555-5533';
-- Conclusion : The Theif is BRUCE ,he escaped to NYC and the accomplice is ROBIN!

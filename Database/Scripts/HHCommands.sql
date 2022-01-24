CREATE DATABASE HORIZON_HOTELS;
use HORIZON_HOTELS;
SELECT * FROM CUSTOMER;
SELECT * FROM RESERVATION;
SELECT * FROM HOTEL;
SELECT * FROM ROOM;
DROP TABLE RESERVATION;

SELECT t.customerId, t.hotelCity, m.fName, m.lName, m.ADDRESS, m.DoB
FROM RESERVATION t INNER JOIN CUSTOMER m
ON t.customerId = m.customerId
order by t.customerId;

SELECT t.customerId, t.hotelCity, m.fName, m.lName, m.ADDRESS, m.DoB, e.roomId, e.roomType
FROM RESERVATION t, CUSTOMER m, ROOM e
where t.customerId = m.customerId and t.roomId = e.roomId
order by t.customerId;

SELECT * 
FROM HOTEL
WHERE capacity <
	(SELECT AVG(capacity)
    FROM HOTEL);

UPDATE HOTEL
SET 
	capacity = 80
WHERE
	hotelCity = 'Cardiff';
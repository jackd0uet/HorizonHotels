CREATE DATABASE HH_DB;
use HH_DB;
DROP TABLE hotel;
DROP TABLE bookings;
DROP TABLE customer;
CREATE TABLE hotel (
	roomId INT NOT NULL auto_increment,
    roomType VARCHAR(20) NOT NULL,
	hotelCity VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL,
    fare DOUBLE NOT NULL DEFAULT 100.00,
    PRIMARY KEY (roomId)
    );
    
CREATE TABLE customer (
	customerId INT NOT NULL auto_increment,
    fName VARCHAR(20) NOT NULL,
    lNAme VARCHAR(20) NOT NULL,
    dob date NOT NULL,
    postcode VARCHAR(20) NOT NULL,
    email VARCHAR(32) NOT NULL,
    password VARCHAR(100) NOT NULL,
    PRIMARY KEY (customerId)
    );
    
CREATE TABLE bookings (
	bookingId INT NOT NULL auto_increment,
    customerId INT NOT NULL,
    roomId INT NOT NULL,
    dateBooked date NOT NULL,
    startDate date NOT NULL,
    endDate date NOT NULL,
    guests INT NOT NULL DEFAULT 1,
    totalFare DOUBLE NOT NULL,
    PRIMARY KEY (bookingId),
    FOREIGN KEY (roomId) REFERENCES hotel(roomId),
    FOREIGN KEY (customerId) REFERENCES customer(customerId)
    );
    
DROP TABLE cancelledBookings;
    
CREATE TABLE cancelledbookings (
	bookingId INT NOT NULL,
    customerId INT NOT NULL,
    roomId INT NOT NULL,
    dateBooked DATE NOT NULL,
    startDate DATE NOT NULL,
    endDate DATE NOT NULL,
    dateCancelled DATE NOT NULL,
    guests INT NOT NULL,
    totalFare DOUBLE NOT NULL,
    totalRefunded DOUBLE NOT NULL,
    PRIMARY KEY (bookingId),
    FOREIGN KEY (roomId) REFERENCES hotel(roomId),
    FOREIGN KEY (customerId) REFERENCES customer(customerId)
    );
    
    SELECT * FROM hotel WHERE hotelCity = 'Aberdeen' and roomType = 'Standard';
    SELECT * FROM bookings;
    SELECT COUNT(*) FROM v WHERE startDate = '2022-03-10' and endDate = '2022-03-11' and roomType = 'Standard' and hotelCity = 'Aberdeen';

CREATE VIEW v AS
	SELECT bookings.bookingId, bookings.roomId, bookings.startDate, bookings.endDate, bookings.guests,
    hotel.roomType, hotel.hotelCity
FROM
bookings, hotel
WHERE
bookings.roomId = hotel.roomId;

DROP VIEW v;



select * from v;

select * from hotel;

CREATE VIEW unbooked AS
SELECT *
FROM hotel
WHERE NOT EXISTS (SELECT * FROM bookings WHERE bookings.roomId = hotel.roomId);

SELECT * FROM BOOKINGS WHERE bookingId = 102;

SELECT * FROM cancelledbookings;

ALTER TABLE cancelledbookings
ADD COLUMN currency VARCHAR(20) NOT NULL DEFAULT 'Pounds';

SELECT * FROM bookings;

SELECT COUNT(*) FROM bookings WHERE customerId = 7;
    
    
SELECT * FROM unbooked;
SELECT * FROM bookings;
SELECT * FROM hotel WHERE NOT EXISTS
 (SELECT * FROM bookings WHERE bookings.roomId = hotel.roomId
 and bookings.startDate = '2022-03-10' and bookings.endDate = '2022-03-11') and hotelCity = 'Aberdeen' and roomType = 'Standard';
    
    
INSERT INTO hotel (roomType, hotelCity, address, fare) VALUES ('Family', 'Aberdeen', 'AB13 0AB', 140.00);
INSERT into customer (customerId, fName, lName, address, dob) VALUES (1, 'John', 'Smith', 'TEST', '2000-01-01');
    
DELETE FROM hotel WHERE roomId > 64;
    
SELECT COUNT(*) FROM hotel WHERE roomId =1;

SELECT * FROM customer;
SELECT * FROM bookings;
select * from hotel;
SELECT fName, lName FROM customer where email = 'test@test.com';

SELECT customerId from customer where email = 'jackdouet@gmail.com';

SELECT * FROM v;
SELECT * FROM bookings inner JOIN hotel WHERE bookings.roomId = hotel.roomId;
select b.bookingId, b.customerId, b.roomId, b.dateBooked, b.startDate, b.endDate, b.guests, b.totalFare,
	h.roomType, h.hotelCity, h.address, h.fare
    from bookings b
    join hotel h
    on b.roomId = h.roomId;

drop view FULLBOOKINGINFO;
CREATE VIEW fullbookinginfo as select b.bookingId, b.customerId, b.roomId, b.dateBooked, b.startDate, b.endDate, b.guests, b.totalFare, b.currency,
	h.roomType, h.hotelCity, h.address
    from bookings b
    join hotel h
    on b.roomId = h.roomId;
    
    select * from fullbookinginfo;
    
    DROP TABLE cancelledBookings;
    
    SELECT * FROM bookings;
    DELETE FROM bookings WHERE bookingId = 4;
    SELECT * FROM cancelledBookings;
    SELECT COUNT(*) FROM cancelledBookings WHERE customerId=3;
    SELECT * FROM bookings;
    
    INSERT INTO cancelledBookings(bookingId, customerId, roomId, dateBooked, startDate, endDate, dateCancelled, guests, totalFare, totalRefunded) VALUES
		(1, 3, 1, '2000-01-01', '2000-01-01', '2000-01-01', '2000-01-01', 1, 140, 140);
        
        

ALTER TABLE hotel
ADD COLUMN offPeakFare DOUBLE NOT NULL DEFAULT 50.00;

SELECT * FROM hotel LIMIT 900, 2000;

UPDATE hotel
SET
	offPeakFare = 60
WHERE
	hotelCity = 'Aberdeen';
    

INSERT INTO hotel(roomType, hotelCity, address, fare, offPeakFare) VALUES ('Standard', 'Bristol', 'BS1 1SD', 140, 70);

DELETE FROM hotel WHERE hotelCity = 'Norwich';

SELECT * FROM bookings;
ALTER TABLE customer
ADD COLUMN userType VARCHAR(20) NOT NULL DEFAULT 'STANDARD';

USE HH_DB;

SELECT * FROM HOTEL LIMIT 0,2000;
UPDATE hotel SET offPeakFare = 50 WHERE roomType = "Double" and hotelCity = "Swansea";


USE TEST_DB;

CREATE TABLE TEST1 (
 value int not null default 1);

select * from TEST1;

insert into test1(value) values (70);

UPDATE TEST1 SET value = value * 1.5 WHERE value = 60;
    
UPDATE hotel SET fare = fare * 1.2 WHERE roomType = "Double";

UPDATE hotel SET offPeakFare = offPeakFare * 1.2 WHERE roomType = "Double";

ALTER TABLE hotel
ADD COLUMN maxOccupancy INT NOT NULL DEFAULT 1;

UPDATE hotel SET maxOccupancy = 6 WHERE roomType = "Family";

SELECT * FROM bookings;
DELETE FROM bookings WHERE bookingId = 19;
SELECT * FROM hotel;
SELECT fare, offPeakFare from hotel where roomType = "Standard" and hotelCity = "Aberdeen";

ALTER TABLE bookings
ADD COLUMN currency VARCHAR(20) NOT NULL DEFAULT "Pounds";

SELECT * FROM customer;

UPDATE customer SET userType = "ADMIN" WHERE customerId = 6;

SELECT * FROM hotel;

SELECT DISTINCT hotelCity from hotel;

SELECT DISTINCT hotelCity FROM hotel WHERE NOT EXISTS (SELECT * FROM bookings WHERE bookings.roomId = hotel.roomId and bookings.startDate = '01.01.2000' and bookings.endDate = '02.01.2000') and hotelCity = 'Aberdeen' and roomType = 'Standard';
SELECT * FROM fullbookinginfo;

drop view fullbookinginfo;

SELECT * FROM fullbookinginfo WHERE hotelCity = 'Aberdeen' AND startDate BETWEEN '2022-04-19' AND '2022-05-01';

SELECT COUNT(*) FROM hotel WHERE hotelCity = 'Aberdeen';

SELECT * FROM hotel WHERE hotelCity = 'Aberdeen';
INSERT INTO hotel (roomType, hotelCity, address, fare, offPeakFare, maxOccupancy) VALUES ('Family', 'Aberdeen', 'AB13 0AB', 210, 90, 6);

SELECT COUNT(*) FROM v WHERE hotelCity = "Aberdeen" and maxOccupancy <= 1 and startDate = '01.01.2000' and endDate = '01.01.2000';

select * from v;


CREATE TABLE comments(
commentNo INT NOT NULL auto_increment,
fName VARCHAR(20) NOT NULL,
lName VARCHAR(20) NOT NULL,
email VARCHAR(32) NOT NULL,
comments VARCHAR(5000) NOT NULL,
timeLeft VARCHAR(50) NOT NULL,
primary key(commentNo) );
drop table comments;
select * from comments;
INSERT INTO comments(fName, lName, email, comments) VALUES ('John', 'Smith', 'test', 'test');

SELECT DISTINCT FROM hotel WHERE hotelCity = 'Aberdeen';

Select * FROM hotel WHERE hotelCity = 'Hereford';

UPDATE hotel SET address = "AB13 0AB" WHERE hotelCity = "Aberdeen" and roomId = 1;

SELECT * FROM customer;


USE HH_DB;
SELECT * FROM customer;

SELECT * FROM bookings;

SELECT * FROM cancelledbookings;






































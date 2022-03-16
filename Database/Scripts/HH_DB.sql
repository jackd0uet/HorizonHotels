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
	customerId INT NOT NULL,
    fName VARCHAR(20) NOT NULL,
    lNAme VARCHAR(20) NOT NULL,
    address VARCHAR(20) NOT NULL,
    dob date NOT NULL,
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
    
    SELECT * FROM hotel WHERE hotelCity = 'Aberdeen' and roomType = 'Standard';
    SELECT * FROM bookings;
    SELECT COUNT(*) FROM v WHERE startDate = '2022-03-10' and endDate = '2022-03-11' and roomType = 'Standard' and hotelCity = 'Aberdeen';

CREATE VIEW V AS
	SELECT bookings.bookingId, bookings.roomId, bookings.startDate, bookings.endDate,
    hotel.roomType, hotel.hotelCity
FROM
bookings, hotel
WHERE
bookings.roomId = hotel.roomId;

select * from hotel;

CREATE VIEW unbooked AS
SELECT *
FROM hotel
WHERE NOT EXISTS (SELECT * FROM bookings WHERE bookings.roomId = hotel.roomId);
    
    
SELECT * FROM unbooked;
SELECT * FROM bookings;
SELECT * FROM hotel WHERE NOT EXISTS
 (SELECT * FROM bookings WHERE bookings.roomId = hotel.roomId
 and bookings.startDate = '2022-03-10' and bookings.endDate = '2022-03-11') and hotelCity = 'Aberdeen' and roomType = 'Standard';
    
    
INSERT INTO hotel (roomType, hotelCity, address, fare) VALUES ('Family', 'Aberdeen', 'AB13 0AB', 140.00);
INSERT into customer (customerId, fName, lName, address, dob) VALUES (1, 'John', 'Smith', 'TEST', '2000-01-01');
    
DELETE FROM hotel WHERE roomId > 64;
    
SELECT COUNT(*) FROM hotel WHERE roomId =1;


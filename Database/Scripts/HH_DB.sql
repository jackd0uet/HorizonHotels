CREATE DATABASE HH_DB;
use HH_DB;
DROP TABLE hotel;
DROP TABLE bookings;
DROP TABLE customer;
CREATE TABLE hotel (
	roomId INT NOT NULL,
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
	bookingId INT NOT NULL,
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
    
    SELECT * FROM hotel WHERE hotelCity = 'Aberdeen';
    SELECT * FROM bookings;
    
    SELECT * FROM CUSTOMER;
    
    INSERT INTO hotel (roomId, roomType, hotelCity, address, fare) VALUES (1, 'Standard', 'Aberdeen', 'AB13 0AB', 140.00);
    INSERT into customer (customerId, fName, lName, address, dob) VALUES (1, 'John', 'Smith', 'TEST', '2000-01-01');
    
    DELETE FROM bookings WHERE bookingId = 1;
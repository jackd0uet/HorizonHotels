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
    offPeakFare DOUBLE NOT NULL,
    currency VARCHAR(20) NOT NULL,
    PRIMARY KEY (bookingId),
    FOREIGN KEY (roomId) REFERENCES hotel(roomId),
    FOREIGN KEY (customerId) REFERENCES customer(customerId)
    );
    
CREATE TABLE cancelledBookings (
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
    currency VARCHAR(20) NOT NULL,
    PRIMARY KEY (bookingId),
    FOREIGN KEY (roomId) REFERENCES hotel(roomId),
    FOREIGN KEY (customerId) REFERENCES customer(customerId)
    );
    
CREATE TABLE comments(
commentNo INT NOT NULL auto_increment,
fName VARCHAR(20) NOT NULL,
lName VARCHAR(20) NOT NULL,
email VARCHAR(32) NOT NULL,
comments VARCHAR(5000) NOT NULL,
timeLeft VARCHAR(50) NOT NULL,
primary key(commentNo) );
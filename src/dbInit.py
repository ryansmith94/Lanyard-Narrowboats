import sqlite3
# TODO: Add property types.
# TODO: Create test code for this file.
conn = sqlite3.connect("narrowboats.db")

cursor = conn.cursor()

# create table
cursor.execute("""CREATE TABLE customer (
    customerId INT PRIMARY KEY,
    name TEXT,
    address TEXT,
    postCode VARCHAR2(10),
    phoneNumber INT
)""")

# http://stackoverflow.com/questions/4272908/sqlite-date-storage-and-conversion
cursor.execute("""CREATE TABLE job (
    jobId INT PRIMARY KEY,
    customerId INT,
    boatId INT,
    jobDescription TEXT,
    jobStatus TEXT,
    jobDate DATE,
    jobDateCompleted DATE,
    price REAL,
    paid BOOLEAN,
    paymentInfo TEXT,
)""")

cursor.execute("""CREATE TABLE lease (
    customerId INT NOT NULL,
    boatId INT NOT NULL,
    dateFrom DATE NOT NULL,
    dateTo DATE NOT NULL,
    mooringId INT NOT NULL,
    datePurchased DATE NOT NULL,
    price REAL NOT NULL,
    vat INT NOT NULL,
    package BOOLEAN DEFAULT 0,
    paymentInfo TEXT NOT NULL,
    CONSTRAINT pkey PRIMARY KEY (mooringId, datePurchased),
    CONSTRAINT fkeyCustomer FOREIGN KEY (customerId) REFERENCES customer(customerId),
    CONSTRAINT fkeyBoat FOREIGN KEY (boatId) REFERENCES boat(boatId)
)""")

cursor.execute("""CREATE TABLE holidayBooking (
    boatId INT,
    boatName TEXT,
    dateTo DATE,
    dateFrom DATE,
    berth INT,
    available BOOLEAN,
    paymentInfo TEXT,
    CONSTRAINT pkey PRIMARY KEY (boatId, dateFrom)
)""")

# TODO: @Faisal please enter your attribute names below, USING THE SAME FORMAT
cursor.execute("""CREATE TABLE owner (

)""")

cursor.execute("""CREATE TABLE boat (
    boatId INT PRIMARY KEY,
    name TEXT,
    description TEXT
)""")

cursor.execute("""CREATE TABLE part (
    partId INT PRIMARY KEY,
    partQuantity INT,
    partDescription TEXT
)""")

cursor.execute("""CREATE TABLE jobpart (
   jobId INT,
   partId INT,
   CONSTRAINT pkey PRIMARY KEY (jobId, partId)
)""")

cursor.execute("""CREATE TABLE holidayboat (
   boatId INT,
   boatName TEXT,
   purchaseDate DATE,
   maxBerth INT,
   CONSTRAINT pkey PRIMARY KEY (boatId, purchaseDate)
)""")

cursor.close()

conn.commit()
conn.close()

import sqlite3
# TODO: Add constraints.
# TODO: Create test code for this file.
conn = sqlite3.connect("narrowboats.db")
cursor = conn.cursor()

# Drops all the tables before recreating them.
cursor.execute("""DROP TABLE IF EXISTS customer""")
cursor.execute("""DROP TABLE IF EXISTS job""")
cursor.execute("""DROP TABLE IF EXISTS lease""")
cursor.execute("""DROP TABLE IF EXISTS holidayBooking""")
cursor.execute("""DROP TABLE IF EXISTS owner""")
cursor.execute("""DROP TABLE IF EXISTS boat""")
cursor.execute("""DROP TABLE IF EXISTS part""")
cursor.execute("""DROP TABLE IF EXISTS jobPart""")
cursor.execute("""DROP TABLE IF EXISTS holidayBoat""")

# create table
cursor.execute("""CREATE TABLE customer (
    customerId INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    postCode VARCHAR2(10),
    phoneNumber VARCHAR2(11)
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
    paymentInfo TEXT
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

#cursor.execute("""CREATE TABLE owner (

#)""")

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

cursor.execute("""CREATE TABLE jobPart (
   jobId INT,
   partId INT,
   CONSTRAINT pkey PRIMARY KEY (jobId, partId)
)""")

cursor.execute("""CREATE TABLE holidayBoat (
   boatId INT,
   boatName TEXT,
   purchaseDate DATE,
   maxBerth INT,
   CONSTRAINT pkey PRIMARY KEY (boatId, purchaseDate)
)""")

# Example of how to add and retrieve data from the database.
name = "John Smith"
address = "Wheatley or summink"
cursor.execute("""INSERT INTO customer(name, address, postCode, phoneNumber) VALUES (
    ?,
    ?,
    "OX3 7JJ",
    "01927364857"
)""", [name, address])

cursor.execute("""INSERT INTO customer(name, address, postCode, phoneNumber) VALUES (
    ?,
    ?,
    "OX3 7JJ",
    "12345678912"
)""", [name, address])

print(cursor.execute("""SELECT * FROM customer""").fetchall()[1][4])

# Commits and closes the database.
cursor.close()
conn.commit()
conn.close()
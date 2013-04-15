from sqlite3 import connect as sql

conn = sql("narrowboats.db")
cursor = conn.cursor()

# Drops all the tables before recreating them.
cursor.execute("""DROP TABLE IF EXISTS customers""")
cursor.execute("""DROP TABLE IF EXISTS jobs""")
cursor.execute("""DROP TABLE IF EXISTS boats""")
cursor.execute("""DROP TABLE IF EXISTS employees""")
cursor.execute("""DROP TABLE IF EXISTS skills""")
cursor.execute("""PRAGMA foreign_keys=ON;""")

# Create tables.
cursor.execute("""CREATE TABLE customers (
    customerId INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    postCode VARCHAR2(10),
    phoneNumber VARCHAR2(11)
)""")

cursor.execute("""CREATE TABLE employees (
    employeeId INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)""")

cursor.execute("""CREATE TABLE boats (
    boatId INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    ownerId INTEGER,
    description TEXT,
    CONSTRAINT fkeyOwner FOREIGN KEY (ownerId) REFERENCES customers(customerId)
)""")

# http://stackoverflow.com/questions/4272908/sqlite-date-storage-and-conversion
# customerId has been included because the owner of the boat does not necessarily have to be
# the person paying to get the boat fixed. This also allows for multiple owners of the boat.
cursor.execute("""CREATE TABLE jobs (
    jobId INTEGER PRIMARY KEY AUTOINCREMENT,
    customerId INTEGER,
    boatId INTEGER,
    assigneeId INTEGER,
    workHours INTEGER NOT NULL,
    description TEXT DEFAULT '',
    status TEXT NOT NULL,
    date DATE NOT NULL,
    price REAL DEFAULT 0,
    paymentInfo TEXT DEFAULT '',
    CONSTRAINT fkeyCustomer FOREIGN KEY (customerId) REFERENCES customers(customerId),
    CONSTRAINT fkeyBoat FOREIGN KEY (boatId) REFERENCES boats(boatId),
    CONSTRAINT fkeyAssignee FOREIGN KEY (assigneeId) REFERENCES employees(employeeId),
    CONSTRAINT limitHours CHECK ((workHours) > 0),
    CONSTRAINT limitPrice CHECK ((price) >= 0),
    CONSTRAINT limitStatus CHECK ((status) IN ('Holiday', 'Incomplete', 'Complete', 'Paid')),
    CONSTRAINT formatDate CHECK ((date) LIKE '____-__-__'),
    CONSTRAINT limitDate CHECK (DATE(date) >= DATE('now'))
)""")

cursor.execute("""CREATE TABLE skills (
    id INT,
    skill TEXT,
    job BOOLEAN,
    PRIMARY KEY (id, skill, job)
)""")

# Test Customers.
cursor.execute("INSERT INTO customers(name, address, postCode, phoneNumber) VALUES(?, ?, ?, ?)", ["Truman Burbank", "11 Burbank Road, Seahaven", "SH1 11BP", "01998060590"])
cursor.execute("INSERT INTO customers(name, address, postCode, phoneNumber) VALUES(?, ?, ?, ?)", ["Jack Sparrow", "1 First Street, London", "LN1 1FS", "02011052045"])

# Test Boats.
cursor.execute("INSERT INTO boats(name, ownerId, description) VALUES (?, ?, ?)", ["Black Pearl", 2, "East Indiaman Galleon"])
cursor.execute("INSERT INTO boats(name, ownerId, description) VALUES (?, ?, ?)", ["Barnacle", 2, "Pirate ship"])

# Test Employees.
cursor.execute("INSERT INTO employees(name) VALUES(?)", ["Alan Flowers"])
cursor.execute("INSERT INTO employees(name) VALUES(?)", ["Jimmy"])

# Test Jobs.
cursor.execute("""INSERT INTO jobs(description, customerId, boatId, workHours, date, status, assigneeId) VALUES(?, ?, ?, ?, DATE('now'), 'Incomplete', ?)""", ["Broken engine.", 2, 2, 1, 1])

# Commits and closes the database.
cursor.close()
conn.commit()
conn.close()

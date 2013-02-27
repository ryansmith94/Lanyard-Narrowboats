import sqlite3
conn = sqlite3.connect("narrowboats.db")
 
cursor = conn.cursor()
 
# create table
cursor.execute("""CREATE TABLE customer (
    customerId,
    name,
    address,
    postCode,
    phoneNumber
)""")

cursor.execute("""CREATE TABLE job (
    jobId,
    customerId,
    boatId,
    jobDescription,
    jobStatus,
    jobDate,
    jobDateCompleted,
    price,
    paid,
    paymentInfo
)""")

cursor.execute("""CREATE TABLE lease (
    customerId,
    boatId,
    dateFrom,
    dateTo,
    mooringId,
    datePurchased,
    price,
    vat,
    package,
    paymentInfo
)""")

cursor.execute("""CREATE TABLE holidayBooking (
    boatId,
    boatName,
    dateTo,
    dateFrom,
    berth,
    available,
    paymentInfo
)""")

#Faisal please enter your attribute names below, USING THE SAME FORMAT
cursor.execute("""CREATE TABLE owner (

)""")

cursor.close()

conn.commit()
conn.close()

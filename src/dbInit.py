import sqlite3
# TODO: Add property types.
# TODO: Create test code for this file.
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

# TODO: @Faisal please enter your attribute names below, USING THE SAME FORMAT
cursor.execute("""CREATE TABLE owner (

)""")

cursor.execute("""CREATE TABLE boat (
    boatId,
    name,
    description
)""")

cursor.execute("""CREATE TABLE part (
    partId,
    partQuantity,
    partDescription
)""")

cursor.execute("""CREATE TABLE jobpart (
   jobId,
   partId
)""")

cursor.execute("""CREATE TABLE holidayboat (
   boatId,
   boatName,
   purchaseDate,
   maxBerth
)""")

cursor.close()

conn.commit()
conn.close()

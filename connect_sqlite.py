import sqlite3
import pandas as pd

# Connects to an existing database file in the current directory
# If the file does not exist, it creates it in the current directory
db_connect = sqlite3.connect('test.db')

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()



# RELATION 1
# String variable for passing queries to cursor
query = """
    CREATE TABLE IF NOT EXISTS Clinic (
        clinicNo INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        telephone TEXT )
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# Insert row into table
query = """
INSERT INTO Clinic (clinicNo, name, address, telephone) 
VALUES (1, 'Pawsome Clinic 1', '123 Main St', '555-1234')
    """
cursor.execute(query)
query = """
INSERT INTO Clinic (clinicNo, name, address, telephone) 
VALUES (2, 'Pawsome Clinic 2', '456 Elm St', '555-5678')
    """
cursor.execute(query)
query = """
INSERT INTO Clinic (clinicNo, name, address, telephone) 
VALUES (3, 'Pawsome Clinic 3', '789 Oak St', '555-9876')
    """
cursor.execute(query)
query = """
    INSERT INTO Clinic (clinicNo, name, address, telephone) 
    VALUES (4, 'Pawsome Clinic 4', '321 Pine St', '555-4321')
    """
cursor.execute(query)
query = """
INSERT INTO Clinic (clinicNo, name, address, telephone) 
VALUES (5, 'Pawsome Clinic 5', '654 Cedar St', '555-8765')
    """
cursor.execute(query)

# Select data
query = """
    SELECT name, address, telephone FROM Clinic;
    """
cursor.execute(query)

# Extract column names from cursor
column_names = [row[0] for row in cursor.description]


# Fetch data and load into a pandas dataframe
table_data = cursor.fetchall()

# RELATION 2
# String variable for passing queries to cursor
query = """
 CREATE TABLE IF NOT EXISTS Staff (
        staffNo INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        telephone TEXT,
        DOB DATE,
        position TEXT,
        salary REAL,
        clinicNo INTEGER,
        FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
        )
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Staff (staffNo, name, address, telephone, DOB, position, salary, clinicNo) 
    VALUES (1, 'John Smith', '123 Main St', '555-1111', '1980-01-01', 'Veterinarian', 50000, 1)
    """
cursor.execute(query)
query = """
    INSERT INTO Staff (staffNo, name, address, telephone, DOB, position, salary, clinicNo) 
    VALUES (2, 'Jane Doe', '456 Elm St', '555-2222', '1990-05-10', 'Veterinary Assistant', 30000, 2)
    """
cursor.execute(query)
query = """
    INSERT INTO Staff (staffNo, name, address, telephone, DOB, position, salary, clinicNo) 
    VALUES (3, 'Robert Johnson', '789 Oak St', '555-3333', '1985-09-15', 'Receptionist', 25000, 3)
    """
cursor.execute(query)
query = """
    INSERT INTO Staff (staffNo, name, address, telephone, DOB, position, salary, clinicNo) 
    VALUES (4, 'Emily Williams', '321 Pine St', '555-4444', '1988-07-20', 'Veterinarian', 55000, 4)
    """
cursor.execute(query)
query = """
    INSERT INTO Staff (staffNo, name, address, telephone, DOB, position, salary, clinicNo) 
    VALUES (5, 'Michael Brown', '654 Cedar St', '555-5555', '1995-03-05', 'Veterinary Assistant', 32000, 5)
    """
cursor.execute(query)

# Select data
query = """
    SELECT name, position, salary FROM Staff;
    """
cursor.execute(query)

# Extract column names from cursor
column_names2 = [row[0] for row in cursor.description]

table_data2 = cursor.fetchall()

# RELATION 3
# String variable for passing queries to cursor
query = """
    CREATE TABLE IF NOT EXISTS Owner (
        ownerNo INTEGER PRIMARY KEY,
        name TEXT,
        address TEXT,
        telephone TEXT
    )
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Owner (ownerNo, name, address, telephone) 
    VALUES (1, 'David Johnson', '1234 Park Ave', '555-111')
    """
cursor.execute(query)
query = """
    INSERT INTO Owner (ownerNo, name, address, telephone) 
    VALUES (2, 'Jennifer Smith', '5678 Lake St', '555-222')
    """
cursor.execute(query)
query = """
    INSERT INTO Owner (ownerNo, name, address, telephone) 
    VALUES (3, 'Michelle Davis', '9876 River Rd', '555-333')
    """
cursor.execute(query)
query = """
    INSERT INTO Owner (ownerNo, name, address, telephone) 
    VALUES (4, 'Brian Wilson', '4321 Ocean Blvd', '555-444')
    """
cursor.execute(query)
query = """
    INSERT INTO Owner (ownerNo, name, address, telephone) 
    VALUES (5, 'Emily Turner', '8765 Mountain Ave', '555-555')
    """
cursor.execute(query)

# Select data
query = """
    SELECT name, address, telephone FROM Owner;
    """
cursor.execute(query)

# Extract column names from cursor
column_names3 = [row[0] for row in cursor.description]
table_data3 = cursor.fetchall()

# RELATION 4
# String variable for passing queries to cursor
query = """
    CREATE TABLE IF NOT EXISTS Pet (
        petNo INTEGER PRIMARY KEY,
        name TEXT,
        DOB DATE,
        species TEXT,
        breed TEXT,
        color TEXT,
        ownerNo INTEGER,
        clinicNo INTEGER,
        FOREIGN KEY (ownerNo) REFERENCES Owner(ownerNo),
        FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo)
    )
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) 
    VALUES (1, 'Buddy', '2018-05-15', 'Dog', 'Labrador', 'Golden', 1, 1)
    """
cursor.execute(query)
query = """
    INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) 
    VALUES (2, 'Luna', '2019-07-10', 'Cat', 'Siamese', 'White', 2, 2)
    """
cursor.execute(query)
query = """
    INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) 
    VALUES (3, 'Max', '2020-03-22', 'Dog', 'German Shepherd', 'Black and Tan', 3, 3)
    """
cursor.execute(query)
query = """
    INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) 
    VALUES (4, 'Charlie', '2017-11-05', 'Dog', 'Golden Retriever', 'Golden', 4, 4)
    """
cursor.execute(query)
query = """
    INSERT INTO Pet (petNo, name, DOB, species, breed, color, ownerNo, clinicNo) 
    VALUES (5, 'Bella', '2016-09-18', 'Cat', 'Persian', 'Gray', 5, 5)
    """
cursor.execute(query)


# Select data
query = """
    SELECT name, species, breed, color FROM Pet;
    """
cursor.execute(query)

# Extract column names from cursor
column_names4 = [row[0] for row in cursor.description]
table_data4 = cursor.fetchall()

# RELATION 5
# String variable for passing queries to cursor
query = """
    CREATE TABLE IF NOT EXISTS Examination (
        examNo INTEGER PRIMARY KEY,
        chiefComplaint TEXT,
        description TEXT,
        dateSeen DATE,
        actionsTaken TEXT,
        clinicNo INTEGER,
        petNo INTEGER,
        FOREIGN KEY (clinicNo) REFERENCES Clinic(clinicNo),
        FOREIGN KEY (petNo) REFERENCES Pet(petNo)
    )
    """

# Execute query, the result is stored in cursor
cursor.execute(query)

# Insert row into table
query = """
    INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, clinicNo, petNo) 
    VALUES (1, 'Fever', 'Physical examination', '2022-01-05', 'Prescribed antibiotics', 1, 1)
    """
cursor.execute(query)
query = """
    INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, clinicNo, petNo) 
    VALUES (2, 'Sore Throat', 'Strep Test', '2022-03-12', 'Rest and pain medication', 2, 2)
    """
cursor.execute(query)
query = """
    INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, clinicNo, petNo) 
    VALUES (3, 'Vomiting', 'Temperature Taken', '2022-05-20', 'Prescribed special diet and medication', 3, 3)
    """
cursor.execute(query)
query = """
    INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, clinicNo, petNo) 
    VALUES (4, 'Physical', 'Physical testing conducted', '2022-07-08', 'Physical test passed', 4, 4)
    """
cursor.execute(query)
query = """
    INSERT INTO Examination (examNo, chiefComplaint, description, dateSeen, actionsTaken, clinicNo, petNo) 
    VALUES (5, 'Weight Loss', 'Blood work taken and physical exam', '2022-09-15', 'Referred to nutritionist', 5, 5)
    """
cursor.execute(query)

# Select data
query = """
    SELECT chiefComplaint, description, dateSeen FROM Examination;
    """
cursor.execute(query)

# Extract column names from cursor
column_names5 = [row[0] for row in cursor.description]


# Fetch data and load into a pandas dataframe
table_data5 = cursor.fetchall()


df = pd.DataFrame(table_data, columns=column_names)
df2 = pd.DataFrame(table_data2, columns=column_names2)
df3 = pd.DataFrame(table_data3, columns=column_names3)
df4 = pd.DataFrame(table_data4, columns=column_names4)
df5 = pd.DataFrame(table_data5, columns=column_names5)
# Examine dataframe
print(df)
print(df.columns)
print("\n")
print(df2)
print(df2.columns)
print(df3)
print(df3.columns)
print("\n")
print(df4)
print(df4.columns)
print("\n")
print(df5)
print(df5.columns)



# Example to extract a specific column
# print(df['name'])


# Commit any changes to the database
db_connect.commit()

# Close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
db_connect.close()

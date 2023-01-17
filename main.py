import pyodbc
import random

# #Ask for user input
print("Welcome to the SQL Availability Checker.")
server_name = input('Please insert the name of the Database Server\n')
db_name = input('Please insert the name of the Database\n')
username = input('Please insert the name of the Username to conntect to ' + db_name + "\n")
password = input('Please insert the password for the Username' + username + 'to conntect to ' + db_name + "\n")

# Connect to the database
# While or for loop - what's required? With while, x in the first print won't work. 
for x in range(5):
#while True:
    print("This is try " + x)
    print("connection establishment")

    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=server_name;'
        'DATABASE=db_name;'
        'UID=username;'
        'PWD=password'
    )

    if conn:
        print("The connection was established sucessfully.")
        cursor = conn.cursor()
    
        print("data write in")
        # Create a test database
        try:
            cursor.execute('''CREATE TABLE test_users
                        (id INT PRIMARY KEY NOT NULL, 
                        name VARCHAR(255) NOT NULL,
                        age INT NOT NULL);''')
            print("Table test_users created successfully")
        except:
            print("Table test_users already exists.")

        # Add some random content to the test_users table
        for i in range(5):
            cursor.execute("INSERT INTO test_users (id, name, age) \
                        VALUES (" + str(i) + ", 'user" + str(i) + "', " + str(10 + i) + ")")

        # Create another example table
        try:
            cursor.execute('''CREATE TABLE test_items
                        (id INT PRIMARY KEY NOT NULL,
                        name VARCHAR(255) NOT NULL,
                        price REAL NOT NULL);''')
            print("Table test_items created successfully")
        except:
            print("Table test_items already exists.")

        # Add some random content to the test_items table
        for i in range(5):
            cursor.execute("INSERT INTO test_items (id, name, price) \
                        VALUES (" + str(i) + ", 'item" + str(i) + "', " + str(100 + i) + ")")

        # Save and close the connection to the database
        conn.commit()
        conn.close()
        print("connection closed sucessfully")

    print("connection establishment")

    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=server_name;'
        'DATABASE=db_name;'
        'UID=username;'
        'PWD=password'
    )

    if conn:
        print("The connection was established sucessfully.")
        cursor = conn.cursor()
    
        print("dropping data")
        # Drop both test tables
        try:
            cursor.execute('''DROP TABLE test_users;''')
            print("Table test_users dropped successfully")
        except:
            print("Table test_users doesn't exist.")

        try:
            cursor.execute('''DROP TABLE test_items;''')
            print("Table test_users dropped successfully")
        except:
            print("Table test_items doesn't exist.")

        # Save and close the connection to the database
        conn.commit()
        conn.close()
        print("connection closed sucessfully")
    else:
        print("The connection attempt wasn't sucessful. The MSSQL server is either not running or does not exist.")
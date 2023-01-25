import PySimpleGUI as sg
import pyodbc
import time

sg.theme('DarkBlue')   

layout = [  [sg.Text('Welcome to the SQL Availability Checker.')],
            [sg.Text('Please insert the name of the Database Server')], 
            [sg.Input(key='server_name')],
            [sg.Text('Please insert the name of the Database')], 
            [sg.Input(key='db_name')],
            [sg.Text('Please insert the name of the Username to conntect to the database')], 
            [sg.Input(key='Username')],
            [sg.Text('Please insert the password for the Username to conntect to the database')], 
            [sg.Input(key='password', password_char='*')],
            [sg.Text('Please insert the amount of times the connection has to be tested')], 
            [sg.Input(key='amount')],
            [sg.Button('Connect'), sg.Button('Quit')] ,
            [sg.Text(text="Output")],
            [sg.Multiline(size=(70,20), font='Courier 8', expand_x=True, expand_y=True, write_only=True,
                reroute_stdout=True, reroute_stderr=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)]
                      ]
# Create the Window
window = sg.Window('SQL Availability Checker', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
        break
    trys = 0

    if event in ('Connect'):
            amount = values['amount']
            for i in range(int(amount)):
                server_name = values['server_name']
                db_name = values['db_name']
                Username = values['Username']
                password = values['password']
                trys += 1

                if server_name == '' or db_name == "" or Username == "" or password == "" or amount =="":
                    print("One or more values have no input. Please insert the missing values.")
                    break

            
                print("This is try " + str(trys) + '!')
                print("Connection establishment is starting...")

                conn = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=' + server_name + ';'
                    'DATABASE=' + db_name + ';'
                    'UID=' + Username + ';'
                    'PWD=' + password
                )
                time.sleep(0.5)

                if conn:
                    time.sleep(0.5)
                    print("The connection was established sucessfully!")
                    cursor = conn.cursor()

                    time.sleep(0.5)
                    print("Data write in is starting...")
                    # Create a test database
                    try:
                        cursor.execute('''CREATE TABLE test_users
                                    (id INT PRIMARY KEY NOT NULL, 
                                    name VARCHAR(255) NOT NULL,
                                    age INT NOT NULL);''')
                        time.sleep(0.5)
                        print("Table test_users created successfully!")

                        # Add some random content to the test_users table
                        for i in range(5):
                            cursor.execute("INSERT INTO test_users (id, name, age) \
                                        VALUES (" + str(i) + ", 'user" + str(i) + "', " + str(10 + i) + ")")
                    except:
                        time.sleep(0.5)
                        print("Table test_users already exists!")

                    # Create another example table
                    try:
                        cursor.execute('''CREATE TABLE test_items
                                    (id INT PRIMARY KEY NOT NULL,
                                    name VARCHAR(255) NOT NULL,
                                    price REAL NOT NULL);''')
                        time.sleep(0.5)
                        print("Table test_items created successfully!")
                                # Add some random content to the test_items table
                        for i in range(5):
                            cursor.execute("INSERT INTO test_items (id, name, price) \
                                        VALUES (" + str(i) + ", 'item" + str(i) + "', " + str(100 + i) + ")")
                            
                    except:
                        time.sleep(0.5)
                        print("Table test_items already exists!")

                    # Save and close the connection to the database
                    conn.commit()
                    conn.close()
                    time.sleep(0.5)
                    print("Connection was closed sucessfully!")
                
                time.sleep(0.5)
                print("Connection establishment is starting...")

                conn = pyodbc.connect(
                    'DRIVER={ODBC Driver 17 for SQL Server};'
                    'SERVER=' + server_name + ';'
                    'DATABASE=' + db_name + ';'
                    'UID=' + Username + ';'
                    'PWD=' + password
                )

                if conn:
                    time.sleep(0.5)
                    print("The connection was established sucessfully!")
                    cursor = conn.cursor()
                    time.sleep(0.5)
                    print("Data dropping is starting...")
                    # Drop both test tables
                    try:
                        cursor.execute('''DROP TABLE test_users;''')
                        time.sleep(0.5)
                        print("Table test_users dropped successfully!")
                    except:
                        time.sleep(0.5)
                        print("Table test_users doesn't exist!")

                    try:
                        cursor.execute('''DROP TABLE test_items;''')
                        time.sleep(0.5)
                        print("Table test_users dropped successfully!")
                    except:
                        time.sleep(0.5)
                        print("Table test_items doesn't exist!")
                    time.sleep(1)

                    # Save and close the connection to the database
                    conn.commit()
                    conn.close()
                    time.sleep(0.5)
                    print("The connection was closed sucessfully!")
                    time.sleep(1)
                else:
                    time.sleep(0.5)
                    print("The connection attempt wasn't sucessful. The MSSQL server is either not running or does not exist.")

window.close()
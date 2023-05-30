import PySimpleGUI as sg
import pyodbc
import time
import datetime

sg.theme('DarkPurple4')   

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
#
def  log_time_function():
    log_time = datetime.datetime.now()
    log_time_format = log_time.strftime("%d/%m/%Y %H:%M:%S")
    return log_time_format

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit': # if user closes window or clicks cancel
        break

    trys = 0
    amount = values['amount']

    if event in ('Connect'):
        
            server_name = values['server_name']
            db_name = values['db_name']
            Username = values['Username']
            password = values['password']
            log_file = open("log.txt", "a")

                    
            if amount == "":
                print(str(log_time_function()) + " - One or more values have no input. Please insert the missing values.")
                log_file.write(str(log_time_function()) + " - One or more values have no input. Please insert the missing values.\n")

            else:
                for i in range(int(amount)):
                    trys += 1

                    if server_name == '' or db_name == "" or Username == "" or password == "" or amount =="":
                        print(str(log_time_function()) + " - One or more values have no input. Please insert the missing values.")
                        log_file.write(str(log_time_function()) + " - One or more values have no input. Please insert the missing values.\n")
                        break

                    print(str(log_time_function()) + " - This is try " + str(trys) + '!')
                    log_file.write(str(log_time_function()) + " - This is try " + str(trys) + '!\n')
                    print(str(log_time_function()) + " - Connection establishment is starting...")
                    log_file.write(str(log_time_function()) + " - Connection establishment is starting...\n")
                    try:
                        conn = pyodbc.connect(
                                'DRIVER={ODBC Driver 17 for SQL Server};'
                                'SERVER=' + server_name + ';'
                                'DATABASE=' + db_name + ';'
                                'UID=' + Username + ';'
                                'PWD=' + password
                            )
                    except:
                        print(str(log_time_function()) + " - Connection attempt failed!")
                        log_file.write(str(log_time_function()) + " - Connection attempt failed!\n")
                        window.refresh()
                        time.sleep(5)
                        continue

                    time.sleep(0.5)


                    if conn:
                        conn.timeout = 1
                        cursor = conn.cursor()
                        print(str(log_time_function()) + " - The connection was established sucessfully!")
                        log_file.write(str(log_time_function()) + " - The connection was established sucessfully!\n")

                        time.sleep(0.5)
                        print(str(log_time_function()) + " - Data write in is starting...")
                        log_file.write(str(log_time_function()) + " - Data write in is starting...\n")
                        # Create a test database
                        try:
                            cursor.execute('''CREATE TABLE test_users
                                        (id INT PRIMARY KEY NOT NULL, 
                                        name VARCHAR(255) NOT NULL,
                                        age INT NOT NULL);''')
                            time.sleep(0.5)
                            print(str(log_time_function()) + " - Table test_users created successfully!")
                            log_file.write(str(log_time_function()) + " - Table test_users created successfully!\n")
                            # Add some random content to the test_users table
                            for i in range(5):
                                cursor.execute("INSERT INTO test_users (id, name, age) \
                                            VALUES (" + str(i) + ", 'user" + str(i) + "', " + str(10 + i) + ")")
                        except:
                            time.sleep(0.5)
                            print(str(log_time_function()) + " - Table test_users already exists or couldn't be created!")
                            log_file.write(str(log_time_function()) + " - Table test_users already exists or couldn't be created!\n")
                            

                        # Create another example table
                        try:
                            cursor.execute('''CREATE TABLE test_items
                                        (id INT PRIMARY KEY NOT NULL,
                                        name VARCHAR(255) NOT NULL,
                                        price REAL NOT NULL);''')
                            time.sleep(0.5)
                            print(str(log_time_function()) + " - Table test_items created successfully!")
                            log_file.write(str(log_time_function()) + " - Table test_items created successfully!\n")
                                    # Add some random content to the test_items table
                            for i in range(5):
                                cursor.execute("INSERT INTO test_items (id, name, price) \
                                            VALUES (" + str(i) + ", 'item" + str(i) + "', " + str(100 + i) + ")")
                                
                        except:
                            time.sleep(0.5)
                            print(str(log_time_function()) + " - Table test_items already exists or couldn't be created!")
                            log_file.write(str(log_time_function()) + " - Table test_items already exists or couldn't be created!\n")
                            
                        # Save and close the connection to the database
                        try:
                            conn.commit()
                            conn.close()
                            time.sleep(0.5)
                            print(str(log_time_function()) + " - Connection was closed sucessfully!")
                            log_file.write(str(log_time_function()) + " - Connection was closed sucessfully!\n")
                        except:
                            continue
                    
                    time.sleep(0.5)
                    print(str(log_time_function()) + " - Connection establishment is starting...")
                    log_file.write(str(log_time_function()) + " - Connection establishment is starting...\n")

                    conn = pyodbc.connect(
                        'DRIVER={ODBC Driver 17 for SQL Server};'
                        'SERVER=' + server_name + ';'
                        'DATABASE=' + db_name + ';'
                        'UID=' + Username + ';'
                        'PWD=' + password
                    )

                    if conn:
                        time.sleep(0.5)
                        print(str(log_time_function()) + " - The connection was established sucessfully!")
                        log_file.write(str(log_time_function()) + " - The connection was established sucessfully!\n")
                        cursor = conn.cursor()
                        time.sleep(0.5)
                        print(str(log_time_function()) + " - Data dropping is starting...")
                        log_file.write(str(log_time_function()) + " - Data dropping is starting...\n")
                        # Drop both test tables
                        try:
                            cursor.execute('''DROP TABLE test_users;''')
                            time.sleep(0.5)
                            print(str(log_time_function()) + " - Table test_users dropped successfully!")
                            log_file.write(str(log_time_function()) + " - Table test_users dropped successfully!\n")
                        except:
                            time.sleep(0.5)
                            print(str(log_time_function()) + " - Table test_users doesn't exist!")
                            log_file.write(str(log_time_function()) + " - Table test_users doesn't exist!\n")
                            continue

                        try:
                            cursor.execute('''DROP TABLE test_items;''')
                            time.sleep(0.5)
                            print(str(log_time_function()) + " - Table test_items dropped successfully!")
                            log_file.write(str(log_time_function()) + " - Table test_items dropped successfully!\n")
                        except:
                            time.sleep(0.5)
                            print(str(log_time_function()) + " - Table test_items doesn't exist!")
                            log_file.write(str(log_time_function()) + " - Table test_items doesn't exist!\n")
                            continue

                        time.sleep(1)

                        # Save and close the connection to the database
                        try:
                            conn.commit()
                            conn.close()
                            time.sleep(0.5)
                            print(str(log_time_function()) + " - The connection was closed sucessfully!")
                            log_file.write(str(log_time_function()) + " - The connection was closed sucessfully!\n")
                        except:
                            continue
                        time.sleep(1)
                    else:
                        time.sleep(0.5)
                        print(str(log_time_function()) + " - The connection attempt wasn't sucessful. The MSSQL server is either not running or does not exist.")
                        log_file.write(str(log_time_function()) + " - The connection attempt wasn't sucessful. The MSSQL server is either not running or does not exist.\n")
                        continue
            log_file.close()
window.close()
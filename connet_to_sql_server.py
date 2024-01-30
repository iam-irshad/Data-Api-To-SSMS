conn = pyodbc.connect('Driver={SQL Server};'
                    'Server=DESKTOP-2A0D0CU\SQLEXPRESS;'
                    'Database=abc;'
                    'Trusted_Connection=yes;')
cursor = conn.cursor()
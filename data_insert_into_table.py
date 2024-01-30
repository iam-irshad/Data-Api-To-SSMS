def read_csv_and_write_data_into_database_table(input_file_path):
    file = open(input_file_path,encoding='utf8')
    read_file = csv.reader(file)
    # print(read_file)
    list_for_append_final_row = []
    for i in read_file:
        final_row = tuple(i)
        list_for_append_final_row.append(final_row)
    # print(list_for_append_final_row)
    
    # Connect to SQL Server
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-2A0D0CU\SQLEXPRESS;'
                        'Database=abc;'
                        'Trusted_Connection=yes;')
    cursor = conn.cursor()

    # Create Table
    cursor.execute('''
            CREATE TABLE staging.currency_data_table (
                currency_code varchar(max),
                symbol varchar(max),
                name varchar(max),
                symbole_native varchar(max),
                decimal_digits int,
                rounding int,
                code varchar(max),
                icon_name varchar(max),
                name_plural varchar(max),
                type varchar(max),
                countries varchar(max)
                )
                ''')
    # Insert Data Into Table
    insert_query = '''
        INSERT INTO staging.currency_data_table (currency_code, symbol, name, symbole_native, decimal_digits, rounding, code, icon_name, name_plural, type, countries)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''

    for row in list_for_append_final_row:
        # print(row)
        if row[0] == 'currency_code':
            continue
        values = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10])
        cursor.execute(insert_query, values)
        # print(values)
        # break

    conn.commit()
read_csv_and_write_data_into_database_table(file_path)
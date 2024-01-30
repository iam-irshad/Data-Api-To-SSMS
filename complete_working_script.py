import requests
import csv
import os
import pyodbc


def get_data_from_url(apikey,url):
    params = {
        "apikey":apikey
    }
    response = requests.get(url=url,params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data. Status code: {response.status_code}")

# print(get_data_from_url("YdH3zeYkA1CxeAUlU8AJWhMIyAEKF2ePJVBCzoJC","https://api.currencyapi.com/v3/currencies?"))
json_data = get_data_from_url("YdH3zeYkA1CxeAUlU8AJWhMIyAEKF2ePJVBCzoJC","https://api.currencyapi.com/v3/currencies?")
# print(json_data)



def write_url_data_into_csv_file(data):
    current_directory = os.getcwd()
    for k,v in data.items():
        # print(v)

        csv_file_name = "my_csv.csv"
        csv_file_path = os.path.join(current_directory, csv_file_name)
    
    header = list(v.values())[5].keys()
    # print(header)
    rows = [{**{'currency_code': key}, **value} for key, value in v.items()]
    # print(rows)
    final_output = []

    for row in rows:
        if len(row['countries']) > 1:
            for country_code in row['countries']:
                duplicate_dictionary = row.copy()
                duplicate_dictionary['countries'] = [country_code]
                # print(duplicate_dictionary)
                final_output.append(duplicate_dictionary)
        else:
            final_output.append(row)
            # print(rows)
    
    for r in final_output:
        # print(r)
        if 'countries' in r and isinstance(r['countries'], list):
            r['countries'] = ''.join(r['countries'])
    # print(r)        

    with open(f"C:\\Users\\Irshad\\{csv_file_name}", 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=['currency_code'] + list(header))
        
        # Write header
        csv_writer.writeheader()
        
        # Write data
        csv_writer.writerows(final_output)
    return f'Data has been written to {csv_file_name}' ,csv_file_path

# print(write_url_data_into_csv_file(json_data))
file_message, file_path = write_url_data_into_csv_file(json_data)
# print(file_message)
# print(file_path)


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
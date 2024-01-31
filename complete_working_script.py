
from extract_data_from_url import get_data_from_url

from write_url_data_into_csv_file import write_url_data_into_csv_file

json_data = get_data_from_url("YdH3zeYkA1CxeAUlU8AJWhMIyAEKF2ePJVBCzoJC","https://api.currencyapi.com/v3/currencies?")
# print(json_data)

file_message,file_path = write_url_data_into_csv_file(json_data)
# print(file_message,file_path)


from data_insert_into_table import read_csv_and_write_data_into_database_table
read_csv_and_write_data_into_database_table(file_path)

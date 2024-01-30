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
insert_query = '''
    INSERT INTO staging.currency_data_table (currency_code, symbol, name, symbole_native, decimal_digits, rounding, code, icon_name, name_plural, type, countries)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    '''
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
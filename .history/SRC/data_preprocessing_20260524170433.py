def convert_to_clean (df, columns): 
    for column in columns: 
        df[column] = df[column].str.lower()
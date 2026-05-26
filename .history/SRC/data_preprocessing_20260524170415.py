def convert_to_lowerStr (df, columns): 
    for column in columns: 
        df[column] = df[column].str.lower()
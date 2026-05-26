import re
import ast

def convert_to_clean_text (df, columns): 
    for column in columns: 
        df[column] = df[column].str.lower()
        df[column] = df[column].apply (lambda x: re.sub(r'[^\w\s]', '', x))
        df[column] = df[column].str.strip()
    return df


def convert_to_string (text, key ='name'):
    if pd.isna(text):
        return []


import re
import ast
import pandas as pd
def convert_to_clean_text (df, columns): 
    for column in columns: 
        df[column] = df[column].str.lower()
        df[column] = df[column].apply (lambda x: re.sub(r'[^\w\s]', '', x))
        df[column] = df[column].str.strip()
    return df


def extract_names(text, key):
    if pd.isna(text):
        return []

    try:
        items = ast.literal_eval(text)
        return [i[key] for i in items if key in i]
    except (ValueError, SyntaxError, TypeError):
        return []
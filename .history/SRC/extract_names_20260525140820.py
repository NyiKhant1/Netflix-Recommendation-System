import re
import ast
import pandas as pd

def extract_names(text, key):
    if pd.isna(text):
        return []

    try:
        items = ast.literal_eval(text)
        return [i[key] for i in items if key in i]
    except (ValueError, SyntaxError, TypeError):
        return []
    
def extract_director(text):
    if pd.isna(text):
        return []
    try:
        crew_list = ast.literal_eval(text)

        for item in crew_list:
            if item.get('job') == 'Director':
                return item.get('name')

        return None

    except (ValueError, SyntaxError, TypeError):
        return None
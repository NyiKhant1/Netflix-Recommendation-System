import os
def remove_columns(df, columns):
    df.drop(columns = columns, inplace = True)

    return df


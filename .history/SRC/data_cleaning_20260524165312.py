import os
def remove_columns(df, columns):
    df.drop(columns = columns, inplace = True)

    return df

file_path = 'D:\University of Sunderland\Netflix-Spotify-Recommendation-System - Copy\Data\Clean\cleaned_data.csv'
def delete_file ():
    if os.path.exists(file_path):
        os.remove(file_path)
        print("File deleted successfully.")
    else:
        print("File does not exist.")
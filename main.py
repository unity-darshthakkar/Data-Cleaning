import pandas as pd
import re

filename = 'champions.xlsx'
# Load the data from an Excel file
df = pd.read_excel(filename)

# Removing Duplicates
df = df.drop_duplicates()

# Removing Non-Printable Characters
df.columns = [re.sub(r'[^A-Za-z\d\s]+', '', col) for col in df.columns]

# Trimming Spaces
df.columns = [col.strip() for col in df.columns]

# filling missing values
for column in df.columns:
    if df[column].dtype == 'object':
        if not df[column].mode().empty:
            df[column] = df[column].fillna(df[column].mode()[0])
    else:
        df[column] = df[column].fillna(df[column].mean())

# Save the cleaned data to a new Excel file
df.to_excel('cleaned_file_path.xlsx', index=False)

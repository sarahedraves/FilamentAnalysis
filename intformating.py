import pandas as pd
import numpy as np
import re

data = {
    'Column1': np.random.uniform(0, 1000, 100).round(4),
    'Column2': np.random.uniform(0, 1000, 100).round(4),
    'Column3': np.random.uniform(0, 1000, 100).round(4)
}

df = pd.DataFrame(data)
print(df)

df = df.applymap(lambda x: -x if np.random.rand() > 0.5 else x)
print(df)

df['Column1'] = df['Column1'].apply(lambda x: f"{x:+.2e}")

def format_columns(df, column_names):
    for column_name in column_names:
        df[column_name] = df[column_name].apply(lambda x: f"{x:+.2e}")
    return df

df = format_columns(df, ['Column2'])
print(df)

output_folder = '/Users/sarahdraves/Library/CloudStorage/OneDrive-Personal/Documents/Research/GothamWeb/OfflineCode/output'
output_file = f"{output_folder}/formatted_data.csv"

df.to_csv(output_file, index=False)
print(f"DataFrame exported to {output_file}")

def match_string(s):
    pattern = r'^[sS][a-zA-Z0-9]*a[a-zA-Z0-9]*$'
    if len(s) < 5:
        return False
    return re.match(pattern, s) is not None

# Test the function
test_strings = ['sarah', 'start', 'simple', 'santa', 's@rah', 'sara']
matches = [s for s in test_strings if match_string(s)]
print("Matching strings:", matches)
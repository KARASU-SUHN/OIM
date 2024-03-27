import pandas as pd 
import numpy as np
import os
import warnings

warnings.filterwarnings('ignore')
# Get the directory of the current script
base_folder = os.path.dirname(os.path.abspath(__file__))

# Define file paths relative to the base_folder, input and output subfolders
csv_file_path1 = os.path.join(base_folder, 'input', 'aztec.csv')
csv_file_path2 = os.path.join(base_folder, 'input', 'AZtec to OIM.csv')
oim_file_path = os.path.join(base_folder, 'output', 'oim.txt')

#import the data as dataframe
df1 = pd.read_csv(csv_file_path1, header=None)
df2 = pd.read_csv(csv_file_path2, header=None)

#paste the [Grid] data from mapdata to AZtec to OIM
df2.iloc[4:8, 1] = df1.iloc[4:8, 1].values

# Extract the 16th row to use as column headers
new_header = df1.iloc[15]  # Extract the 16th row (0-based indexing)

# Select rows from the 17th row to the end
new_df1 = df1[16:]  

# Set the extracted 16th row as the column headers for the new DataFrame
new_df1.columns = new_header  # Set the new headers

# Reset the index of the new DataFrame if needed
new_df1.reset_index(drop=True, inplace=True)

#drop NaN
df1_cleaned = new_df1.dropna(axis=1, how='all')


# Convert 'Euler1', 'Euler2', 'Euler3' to numeric types
# errors='coerce' will replace non-convertible values with NaN
df1_cleaned['Euler1'] = pd.to_numeric(df1_cleaned['Euler1'], errors='coerce')
df1_cleaned['Euler2'] = pd.to_numeric(df1_cleaned['Euler2'], errors='coerce')
df1_cleaned['Euler3'] = pd.to_numeric(df1_cleaned['Euler3'], errors='coerce')

# convert the column "Euler1","Euler2","Euler3" degrees data to radians data
df1_cleaned['Euler1_arc'] = df1_cleaned['Euler1'] * np.pi / 180
df1_cleaned['Euler2_arc'] = df1_cleaned['Euler2'] * np.pi / 180
df1_cleaned['Euler3_arc'] = df1_cleaned['Euler3'] * np.pi / 180

#rearranege columns
df_OIM = df1_cleaned[['Euler1_arc', 'Euler2_arc', 'Euler3_arc', 'X', 'Y', 'BC', 'MAD', 'Phase']]


df2_file_path = os.path.join(base_folder, 'df2.txt')

#save df2 as txt file
df2.to_csv(df2_file_path, sep="\t", index=False,header=None)
        
df_OIM_file_path = os.path.join(base_folder, 'df_OIM.txt')

#save df_OIM as txt file
df_OIM.to_csv(df_OIM_file_path, sep="\t", index=False,header=None)  

#save the result in the txt file
with open(oim_file_path, 'w') as oim_file:
    with open(df2_file_path, 'r') as df2_file:
        oim_file.write(df2_file.read())
#     oi_file.write("\n")  # Optionally add a newline for separation
    with open(df_OIM_file_path, 'r') as df_OIM_file:
        oim_file.write(df_OIM_file.read())

print(f'oim file saved to: {oim_file_path}')  

try:
    os.remove(df2_file_path)
except FileNotFoundError:
    print(f"The file {df2_file_path} does not exist.")
except PermissionError:
    print(f"Permission denied: unable to delete {df2_file_path}.")
except Exception as e:
    print(f"Error occurred: {e}.")

try:
    os.remove(df_OIM_file_path)
except FileNotFoundError:
    print(f"The file {df_OIM_file_path} does not exist.")
except PermissionError:
    print(f"Permission denied: unable to delete {df_OIM_file_path}.")
except Exception as e:
    print(f"Error occurred: {e}.")
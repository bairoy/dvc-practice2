import pandas as pd
import os
data = {'Name':['Alice','Bob','Charlie'],'Age':[24,30,35],'City':['New York','Los Angeles','Chicago']}
df = pd.DataFrame(data)

# # Adding new row to df for V2
new_row_loc = {'Name': 'GF1', 'Age': 20, 'City': 'City1'}
df.loc[len(df.index)] = new_row_loc

data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)

file_path = os.path.join(data_dir,'sample_data.csv')

df.to_csv(file_path,index=False)

print(f"CSV file saved to {file_path}")
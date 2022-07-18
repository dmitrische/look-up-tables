import pandas as pd

url="https://www.legislation.govt.nz/regulation/public/2008/0355/latest/DLM1633733.html"

dfs = pd.read_html(url)

if len(dfs) != 4:
    exit('Unexpected number of dataframes!')
else:
    filenames=['table1','table2','table3','table4']
    
# Convert strings to floats and remove the unnecesary space,
# i.e. '1 000' -> 1000.0, but only in first dataframe.
for col in dfs[0].columns[1:]:
    dfs[0][col] = [float(str(val).replace(" ", "")) for val in dfs[0][col].values]

# Remove blank colum in second dataframe.
dfs[1].drop("Unnamed: 4", axis=1, inplace=True)

# Write the four dataframes to files
for i in range(4):
    dfs[i].to_csv(filenames[i]+'.csv', index=False)


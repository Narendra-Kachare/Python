"""
    Dataframes using python : panda2
"""

import pandas as pd

data = [{'Name': 'PPA',  'Duration': 4, 'Fees':18500},{'Name': 'LB', 'Duration': 3, 'Fees':18500},{'Name': 'Angular', 'Duration': 3, 'Fees':18500},{'Name': 'Python', 'Duration': 3, 'Fees':18500}]
df = pd.DataFrame(data)
print(df)


writer = pd.ExcelWriter('MarvellousPands.xlsx',engine='xlsxwriter')
df.to_excel( writer,sheet_name='Sheet1')
writer.close()      # replace .save() method with .close method()

print("Excel file is generated Successfully")

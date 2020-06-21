import pandas as pandu
from openpyxl import Workbook  # To save .xlsx file using pandas dataFrame
path = '/Users/VikramSingh/Pictures/PythonLearning/Pandas/Python.xlsx'
base_df = pandu.read_excel(path)
update_df = base_df[base_df['Age']>23]
print(update_df)  #The record having age greater than 23
write_path = '/Users/VikramSingh/Pictures/PythonLearning/Pandas/Python_Updated.csv' # save in .csv file
update_df.to_csv(write_path)
update_df.to_excel('/Users/VikramSingh/Pictures/PythonLearning/Pandas/PythonUpdated.xlsx') # sve in .xlsx file


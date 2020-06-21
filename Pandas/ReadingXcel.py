import pandas as pandu
path = '/Users/VikramSingh/Pictures/PythonLearning/Pandas/Python.xlsx'
data_frame = pandu.read_excel(path)
print(data_frame.head())
print(data_frame[['Name','Age']])
print(data_frame[0:2])
# Accessing unique element using .iloc
df = pandu.DataFrame(data_frame)
print(df.iloc[0,1]) # It will print value of first row and second column --  Male
print(data_frame.iloc[0,0]) #It will print value of first row first column  -- Anuj Singh
print(df.iloc[:1,2:])
print(df.iloc[3:,0:2]) # It will print rows from index = 3 and above , and column from index = 0 to 1 
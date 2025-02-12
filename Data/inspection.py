import pandas as pd

#Import the data and make dataframe
data = pd.read_csv('exercise_ver3.csv')

#Print all values in column "muscle_gp"
print(data['muscle_gp'].unique())
print(len(data['muscle_gp'].unique()))

print(data['Equipment'].unique())
#Identify all exercises with nan equipment values
print(data[data['Equipment'].isnull()])


#Identify duplicate exercise names
'''for i in data['Exercise_Name'].unique():
    if len(data[data['Exercise_Name'] == i]) > 1:
        print(i)'''

import pandas 
import string



Bikes = pandas.read_csv('data.csv', skipinitialspace=True, encoding ='utf-8')

print(pandas.Series(Bikes['Make'].value_counts()[:3].index))
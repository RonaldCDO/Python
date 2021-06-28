import pandas as pd

dict = {
    'country': ['Brazil', 'Russia', 'India', 'China', 'South Africa'],
    'capital': ['Brasilia', 'Moscow', 'New Delhi', 'Beijing', 'Pretoria'],
    'area': [8.516, 17.10, 3.286, 9.597, 1.221],
    'population': [200.4, 143.5, 1252, 1357, 52.98]}

print(dict)

brics = pd.DataFrame(dict)

print(brics, '\n')

brics.index = ['BR', 'RU', 'IN', 'CH', 'SA']
print(brics, '\n')

brics = pd.read_csv('brics.csv', index_col=0)
print(brics, '\n')

print(brics['country'], '\n')  # series -> 1D array, Column Access []
print(type(brics['country']))
print(brics[['country']], '\n')  # DataFrame -> 2D array
print(type(brics[['country']]), '\n')
print(brics[['country', 'capital']], '\n')  # DataFrame -> 2D array
print(brics[0:], '\n')  # slice -> take the Rows Access[]

'''
    loc -> access data using row labels
    iloc -> access data using position or index
'''

# loc
print('->Start_loc<-')
print(brics.loc['RU'], '\n')  # row as pandas Series
print(brics.loc[['RU']], '\n')  # row as pandas DataFrame
print(brics.loc[['RU', 'IN', 'CH']], '\n')  # rows as pandas DataFrame
print(brics.loc[['RU', 'IN', 'CH'], ['country', 'capital']], '\n')  # rows ans Columns as pandas DataFrame
print(brics.loc[:, ['country']])  # first parameter is rows and second columns
print('->End_loc<-', '\n')

# iloc
print(brics.iloc[1])  # row as pandas Series
print(brics.iloc[[1, 2, 3]])  # rows as pandas DataFrame
print(brics.iloc[:, [0, 1]])  # rows and columns as pandas DataFrame
print(brics.iloc[:, :])  # rows and columns

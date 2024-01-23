import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrels = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels = len(data[data['Primary Fur Color'] == 'Black'])
print()

data_dict = {
    'Fur Color': ['Gray', 'Red', 'Black'],
    'Count': [gray_squirrels, red_squirrels, black_squirrels]
}
dataframe = pandas.DataFrame(data_dict)
print(dataframe)

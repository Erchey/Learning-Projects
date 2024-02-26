import pandas

data = pandas.read_csv("weather_data.csv")
max_temp = data.temp == data.temp.max()
data_dict = data.to_dict()
print(data[max_temp])

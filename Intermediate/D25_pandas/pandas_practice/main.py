# with open("Intermediate/D25_pandas/weather_data.csv",) as data:
#     weather = data.readlines()
#     print(weather)


# # csv operations
# import csv

# with open("Intermediate/D25_pandas/weather_data.csv") as data:
#     data = csv.reader(data)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("Intermediate/D25_pandas/weather_data.csv")
# print(data['temp'])

# data_dict = data.to_dict()
# # print(data_dict)

# temp_list = data['temp'].to_list()

# print(temp_list)

# print(data['temp'].mean())
# print(data['temp'].max())
# print(data)

# print(data[data.temp == data.temp.max()])

data_dict = {
    "students": ["a", "b", "c"],
    "score": [1, 2, 3]
}

data1 = pandas.DataFrame(data_dict)
print(data1)

data1.to_csv("Intermediate/D25_pandas/new_data.csv")
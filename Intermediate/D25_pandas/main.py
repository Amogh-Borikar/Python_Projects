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
print(data['temp'])
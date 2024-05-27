import pandas as pd

data = pd.read_csv("Intermediate/D25_pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240526.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black_count = len(data[data["Primary Fur Color"] == "Black"])

# print(gray_count, Cinnamon_count, Black_count)

data_dict = {
    "Primary Fur Color": ["Gray", "Cinnamon", "Black"],
    "count": [gray_count, Cinnamon_count, Black_count]
}

count_data = pd.DataFrame(data_dict)

print(count_data)

count_data.to_csv("Intermediate/D25_pandas/squirrel_count_data.csv")
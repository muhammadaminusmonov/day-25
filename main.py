# with open("weather_data.csv") as csv_data:
#     data = csv_data.readlines()
# print(data)


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas
#
# # data = pandas.read_csv("weather_data.csv")
# #
# #
# # # data_dic = data.to_dict()
# # # temp_list = data["temp"].to_list()
# # #
# # # print(data["temp"].mean())
# # #
# # # print(data["temp"].max())
# # #
# # # # Get data in columns
# # # print(data["condition"])
# # # print(data.condition)
# #
# # # print(data[data.day == "Monday"])
# # #
# # # print(data[data["temp"] == data.temp.max()])
# #
# # # monday = data[data.day == "Monday"]
# # # print(monday.condition)
# # # print(monday.temp * 9 / 5 + 32)
#
# data_dic = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dic)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240722.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "colors": ["gray", "cinnamon", "black"],
    "count": [gray, cinnamon, black]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel.csv")

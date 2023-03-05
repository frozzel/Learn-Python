#import csv

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#          temp.append(int(row[1]))
         
#     print(temp)
    
import pandas

# data = pandas.read_csv("weather_data.csv")

# print(data)
# print(data["day"])

# data_dict  = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

# Sum = sum(temp_list)
# Average = round(Sum/len(temp_list))
# print(Average)

# print(data['temp'].mean())

# print(data['temp'].max())

# # get data in column

# print(data['condition'])
# # or #
# print(data.condition)

# Get rows

# print(data[data.day == 'Monday'])
# print(data[data.temp  == data.temp.max()])

# monday = data[data.day == "Monday"]
# conversion = float(monday.temp * 1.8) + 32
# print(f"Mondays Temp in Fahrenheit: {conversion}")

# create a dataframe from scratch --------------------------

# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76,56,65]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# print(data)

data = pandas.read_csv("2018.csv")

gray_sqs = len(data[data["Primary Fur Color"] == "Gray"])
black_sqs = len(data[data["Primary Fur Color"] == "Black"])
red_sqs = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(gray_sqs, black_sqs, red_sqs)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_sqs, red_sqs, black_sqs]
}

data_sqs = pandas.DataFrame(data_dict)
data_sqs.to_csv("Data_Squirrels.csv")


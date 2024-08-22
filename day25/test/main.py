# # import csv
# # with open ("002WEA~1.CSV" , "r") as f:
# #     csv_reader = csv.reader(f)
# #     for line in csv_reader:
# #         print(line)
# # print (data["temp"].max())
# # print(type(data))   
# # print (data[data.temp == data.temp.max()]) 
# # monday = data[data.day == "Monday"]
# # monday_temp = int(monday.temp)
# # print(monday_temp*9/5+32)
# # data_dict = {
# #     "students": ["Amy", "James", "Angela"],
# #     "scores": [76, 56, 65]
# # }
# # data = pd.DataFrame(data_dict)
# # data.to_csv("new_data.csv")
# import pandas as pd
# data = pd.read_csv("004201~1.CSV")
# colors = data["Primary Fur Color"]
# black = len(data[colors == "Black"])
# grey = len(data[colors == "Gray"])
# red = len(data[colors == "Cinnamon"])
# data_frame = {
#     "Fur Color": ["Black", "Grey", "Red"],
#     "Count": [black, grey, red]
# }
# pd.DataFrame(data_frame).to_csv("squirrel_count.csv")
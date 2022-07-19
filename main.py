import pandas as pan

data = pan.read_csv("weather-data.csv")
print(data["temp"])

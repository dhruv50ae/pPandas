import pandas as pan

data = pan.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

furEnt = ["Gray", "Red", "Black"]

blackCount = len(data[data["Primary Fur Color"] == "Black"])
grayCount = len(data[data["Primary Fur Color"] == "Gray"])
redCount = len(data[data["Primary Fur Color"] == "Cinnamon"])

print(blackCount)
print(grayCount)
print(redCount)

finDict = {
    "Fur Color" : furEnt,
    "Count" : [grayCount, redCount, blackCount]
}

finData = pan.DataFrame(finDict)

print(finData.to_csv("sColorCount.csv"))
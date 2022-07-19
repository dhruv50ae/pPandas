import pandas as pan

data = pan.read_csv("weather-data.csv")

dataDict = {
    "students" : ["Alpha", "Beta", "Charlie"],
    "scores" : [76, 56, 65]
}
dataF = pan.DataFrame(dataDict)

dataF.to_csv("newData.csv")
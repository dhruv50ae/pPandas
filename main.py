import turtle
import pandas

screen = turtle.Screen()
screen.title("USA States Game")
image = "download.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
allStates = data["state"].to_list()

guessedStates = []

while len(guessedStates) < 50:
    answerState = screen.textinput(title=f"{len(guessedStates)}/50 states correct", prompt="What is another state's name?").title()
    if answerState in allStates:
        guessedStates.append(answerState)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        sd = data[data.state == answerState]
        t.goto(int(sd.x), int(sd.y))
        t.write(sd.state.item())

screen.exitonclick()

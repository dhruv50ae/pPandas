import turtle

screen = turtle.Screen()
screen.title("USA States Game")
image = "download.gif"
screen.addshape(image)
turtle.shape(image)

answerState - screen.textinput(title="Guess teh state", prompt="What is another state's name?")

# def getMouseClickCoor(x, y):
#     print(x, y)
# turtle.onscreenclick(getMouseClickCoor)
# turtle.mainloop()

# screen.exitonclick()
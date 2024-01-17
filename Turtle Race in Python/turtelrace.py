from turtle import Turtle, Screen
import random

is_race_on = False

#Screen Setup | Accepts user input and lists colors and turtles
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
#co-ordinate of the first turtle along the Y-coordinate
y_cord = -100

#Detects if the user bet of not
if user_bet:
    is_race_on = True

#creates the turtles and lines them up along the Y-axis with distance of 40 paces
def startingline(colorof):    
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colorof)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cord)
    all_turtles.append(new_turtle)

for color in colors:
    startingline(color)
    y_cord += 40

#A loop that runs until the race ends, works using a boolean
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                # print(f"You have won! The {winning_color} turtle has won the race.")
                screen.title(f"You have won! The {winning_color} turtle has won the race.")
            else:
                # print(f"You have lost! The {winning_color} turtle has won the race.")
                screen.title(f"You have lost! The {winning_color} turtle has won the race.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()

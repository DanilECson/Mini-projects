from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height=400)
screen.title("Tempest: Bet your turtle!!!")
print(f"Guide: press 'w' to get white screen,'b' for black screen and 'd' for dark blue screen")
def whitebg():
    screen.bgcolor("white")
def blackbg():
    screen.bgcolor("black")
def bluebg():
    screen.bgcolor("dark blue")
user_bet = screen.textinput(title = "Tempest", prompt="Which turtle do you think will win? : ")
screen.listen()
screen.onkey(key="w",fun=whitebg)
screen.onkey(key = "b",fun = blackbg)
screen.onkey(key = "d",fun = bluebg)
color = ["red","orange","yellow","green","blue","indigo","pink","violet"]
y_position = [-70,-40,-10,20,50,80,110,140]
all_turtles = []
for range in range(0,8):
    tim = Turtle(shape = "turtle")
    tim.penup()
    tim.color(color[range])
    tim.goto(x = -220,y =y_position[range] )
    all_turtles.append(tim)
end = True
while end:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            end = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won the {user_bet}  turtle won!")
                end = True
            else:
                print(f"You lose the {winning_color} turtle won!")
        random_distance = random.randint(1,11)
        turtle.forward(random_distance)
screen.exitonclick()




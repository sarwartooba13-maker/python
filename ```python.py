```python
import turtle
import random
import time

# Screen setup
screen = turtle.Screen()
screen.title("Python Car Racing Game")
screen.setup(width=600, height=700)
screen.bgcolor("dark green")
screen.tracer(0)

# Road
road = turtle.Turtle()
road.hideturtle()
road.speed(0)
road.penup()
road.goto(-200, -350)
road.color("gray")
road.begin_fill()

for _ in range(2):
    road.forward(400)
    road.left(90)
    road.forward(700)
    road.left(90)

road.end_fill()

# Road boundaries
def draw_line(x, y, length, color, width):
    line = turtle.Turtle()
    line.hideturtle()
    line.penup()
    line.goto(x, y)
    line.color(color)
    line.pensize(width)
    line.setheading(90)
    line.pendown()
    line.forward(length)
    line.penup()
    return line

draw_line(-200, -350, 700, "white", 4)
draw_line(200, -350, 700, "white", 4)

# Animated middle road markings
road_lines = []

for y in range(-330, 350, 100):
    line = turtle.Turtle()
    line.shape("square")
    line.color("white")
    line.shapesize(stretch_wid=0.4, stretch_len=3)
    line.penup()
    line.goto(0, y)
    road_lines.append(line)

# Player car
player = turtle.Turtle()
player.shape("square")
player.color("deepskyblue")
player.shapesize(stretch_wid=2, stretch_len=1)
player.penup()
player.goto(0, -250)

# Opponent cars
cars = []
car_colors = ["red", "yellow", "orange", "purple", "pink"]

for _ in range(3):
    car = turtle.Turtle()
    car.shape("square")
    car.shapesize(stretch_wid=2, stretch_len=1)
    car.penup()
    car.color(random.choice(car_colors))
    car.goto(random.choice([-140, -70, 70, 140]),
             random.randint(100, 600))
    cars.append(car)

# Score display
score = 0

score_text = turtle.Turtle()
score_text.hideturtle()
score_text.color("white")
score_text.penup()
score_text.goto(-275, 310)

def update_score():
    score_text.clear()
    score_text.write(
        f"Score: {score}",
        font=("Arial", 18, "bold")
    )

update_score()

# Game state
game_running = True
game_over = False

# Player controls
def move_left():
    if game_running and not game_over:
        x = player.xcor()
        if x > -165:
            player.setx(x - 30)

def move_right():
    if game_running and not game_over:
        x = player.xcor()
        if x < 165:
            player.setx(x + 30)

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# Game over message
message = turtle.Turtle()
message.hideturtle()
message.color("white")
message.penup()

def show_game_over():
    global game_over
    game_over = True

    message.goto(0, 40)
    message.write(
        "GAME OVER",
        align="center",
        font=("Arial", 30, "bold")
    )

    message.goto(0, -10)
    message.write(
        f"Final Score: {score}",
        align="center",
        font=("Arial", 18, "normal")
    )

    message.goto(0, -55)
    message.write(
        "Press R to Restart",
        align="center",
        font=("Arial", 16, "normal")
    )

def restart_game():
    global score, game_over

    if game_over:
        score = 0
        player.goto(0, -250)

        for car in cars:
            car.color(random.choice(car_colors))
            car.goto(
                random.choice([-140, -70, 70, 140]),
                random.randint(350, 700)
            )

        for index, line in enumerate(road_lines):
            line.goto(0, -330 + index * 100)

        message.clear()
        game_over = False
        update_score()

screen.onkeypress(restart_game, "r")
screen.onkeypress(restart_game, "R")

# Main animation loop
while True:
    screen.update()

    if not game_over:
        # Move road markings
        for line in road_lines:
            line.sety(line.ycor() - 8)

            if line.ycor() < -350:
                line.sety(350)

        # Move opponent cars
        for car in cars:
            car.sety(car.ycor() - 7)

            # Respawn cars after passing the player
            if car.ycor() < -370:
                car.goto(
                    random.choice([-140, -70, 70, 140]),
                    random.randint(400, 700)
                )
                car.color(random.choice(car_colors))

                score += 1
                update_score()

            # Collision detection
            if (
                abs(player.xcor() - car.xcor()) < 25
                and abs(player.ycor() - car.ycor()) < 35
            ):
                show_game_over()
                break

    time.sleep(0.02)
```

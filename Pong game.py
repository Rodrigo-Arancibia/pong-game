import turtle
import winsound     # For managing the game sounds

# Game screen resolution
WIDTH = 800
HEIGHT = 600

# Helpful variables
WIDTH_half = WIDTH/2
HEIGHT_half = HEIGHT/2

wn = turtle.Screen()
wn.title("Pong game by Rodrigo Arancibia")
wn.bgcolor("black")
wn.setup(width = WIDTH, height = HEIGHT)
wn.tracer(0)

# Score
score_a = 0
score_b = 0



# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(3) # Speed animation for the turtle module. Sets the speed to maximum possible speed.
paddle_a.shape("square")
paddle_a.color("white")
# By default, this shape is 20 px wide by 20 px height. In this line I stretch the shape.
# So I redefine the shape by 5 times the wid => 5 * 20 px = 100 px and 1 time the length => 1 * 20 px = 20 px
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
# Turtles, by definition, draw a line as they move. We dont need to draw a line because that's not my this program does.
paddle_a.penup()
# I want my paddle "A" to start at x = -350 and y = 0  (vertically centered on the screen and at the left side of it).
# In this game (0, 0) is in the middle, (-350, 0) is in the left center and (350, 0) is in the right center.
paddle_a.goto(-350, 100)



# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # Speed animation for the turtle module. Sets the speed to maximum possible speed.
paddle_b.shape("square")
paddle_b.color("white")
# By default, this shape is 20 px wide by 20 px height. So in this line I stretch the shape.
# So I redefine the shape by 5 times the wid => 5 * 20 px = 100 px and 1 time the length => 1 * 20 px = 20 px
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
# Turtles, by definition, draw a line as they move. We dont need to draw a line because that's not my this program does.
paddle_b.penup()
# I want my paddle "B" to start at x = 350 and y = 0 (vertically centered on the screen and at the right side of it).
# In this game (0, 0) is in the middle, (-350, 0) is in the left center and (350, 0) is in the right center.
paddle_b.goto(350, 0)



# Ball
ball = turtle.Turtle()
ball.speed(0) # Speed animation for the turtle module. Sets the speed to maximum possible speed.
ball.shape("circle")
ball.color("white")
# Turtles, by definition, draw a line as they move. We dont need to draw a line because that's not my this program does.
ball.penup()
# I want my ball to start in the middle of the screen (vertically and horizontally centered on the screen).
ball.goto(0, 0)

# Every time the ball moves it moves by 2 px.
ball.dx = 0.5     # Delta moving in 'x'
ball.dy = 0.5     # Delta moving in 'y'



# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))



# Function declarations
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)



# Keyboard binding
wn.listen()     # Tells the program to listen for keyboard input
wn.onkeypress(paddle_a_up, "w")     # When the users presses 'w', call the function paddle_a_up()
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")     # When the users presses 'Up', call the function paddle_b_up()
wn.onkeypress(paddle_b_down, "Down")



# Main game loop
while True:

    wn.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Border checking

    # (Ball) Top border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1    # It reverses the direction of the ball.

    # (Ball) Bottom border
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1    # It reverses the direction of the ball.

    # (Ball) Right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        # TODO Mejorar para que detecte este archivo.
        winsound.PlaySound("Missed.wav", winsound.SND_ASYNC) # Plays a sound when the ball does not touch the right paddle
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))


    # (Ball) Left border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        winsound.PlaySound("Missed.wav", winsound.SND_ASYNC) # Plays a sound when the ball does not touch the left paddle
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))



    # (Paddle 'A') Top border
    if paddle_a.ycor() + 50 > HEIGHT/2:
        paddle_a.goto(-350, 250)

    # (Paddle 'A') Bottom border
    if paddle_a.ycor() - 50 < - HEIGHT/2:
        paddle_a.goto(-350, -250)

    # (Paddle 'B') Top border
    if paddle_b.ycor() + 50 > 300:
        paddle_b.goto(350, 250)
    
    # (Paddle 'B') Bottom border
    if paddle_b.ycor() - 50 < -300:
        paddle_b.goto(350, -250)



    # Paddle and ball collisions

    # Paddle 'A':
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("PlayerA.wav", winsound.SND_ASYNC)   # Plays a sound

    # Paddle 'B':
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("PlayerB.wav", winsound.SND_ASYNC)   # Plays a sound
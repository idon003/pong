
import turtle

window = turtle.Screen() 

window.title("Play me!")
window.bgcolor("black")
window.setup(width=800, height= 600)
window.tracer(0)


first_point, second_point = 0, 0 



# first paddle
first_paddle = turtle.Turtle()
first_paddle.speed(0)
first_paddle.shape('square')
first_paddle.shapesize(stretch_wid=5, stretch_len=1)
first_paddle.color('white')
first_paddle.penup()
first_paddle.goto(-350, 0)


# second paddle
second_paddle = turtle.Turtle()
second_paddle.speed(0)
second_paddle.shape('square')
second_paddle.shapesize(stretch_wid=5, stretch_len=1)
second_paddle.color('white')
second_paddle.penup()
second_paddle.goto(350, 0)

# ball

ball = turtle.Turtle()
ball.speed(10)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = ball.dy = 0.5


# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)


pen.write(f'Player A:{first_point} Player B: {second_point}', align='center', font = ('Coutier', 24, 'normal'))

# Moves

def first_paddle_up():
    y = first_paddle.ycor()
    y += 20
    first_paddle.sety(y)

def first_paddle_down():
    y = first_paddle.ycor()
    y -= 20
    first_paddle.sety(y)

def second_paddle_up():
    y = second_paddle.ycor()
    y += 20
    second_paddle.sety(y)

def second_paddle_down():
    y = second_paddle.ycor()
    y -= 20
    second_paddle.sety(y)





window.listen()
window.onkeypress(first_paddle_up, 'w')
window.onkeypress(first_paddle_down, 's')
window.onkeypress(second_paddle_up, 'Up')
window.onkeypress(second_paddle_down, 'Down')
# Main game loop

while True:
    window.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        first_point += 1
        pen.clear()
        pen.write(f'Player A:{first_point} Player B: {second_point}', align='center', font = ('Coutier', 24, 'normal'))
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        second_point += 1
        pen.clear()
        pen.write(f'Player A:{first_point} Player B: {second_point}', align='center', font = ('Coutier', 24, 'normal'))
        ball.goto(0,0)
        ball.dx *= -1
    # bounce

    if (ball.xcor() > 340) and (ball.ycor() < second_paddle.ycor() + 40 and ball.ycor() > second_paddle.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340) and (ball.ycor() < first_paddle.ycor() + 40 and ball.ycor() > first_paddle.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
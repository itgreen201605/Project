import turtle
import math
slowpoke = turtle.Turtle()
speedy = turtle.Turtle()
slowpoke.forward(100)
speedy.circle(100)
speedy.right(90)
speedy.forward(100)
print(slowpoke.position())
print(speedy.position())
slowpoke_coords = slowpoke.position()
print(speedy.towards(slowpoke_coords))
new_heading = speedy.towards(slowpoke_coords)
speedy.setheading(new_heading)
speedy.forward(math.sqrt(20000))
speedy.hideturtle()
speedy.clear()
speedy.reset()
speedy.right(90)
speedy.forward(100)
turtle.done()
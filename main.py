# Set up the screen
import turtle
import pygame

pygame.init()

turtle.setup(400, 700)
turtle.bgcolor("black")
turtle.title("Tetris")
turtle.hideturtle()

# Create the shapes
shape_list = []

square = [[1, 1],
          [1, 1]]

shape_list.append(square)

line = [[1, 1, 1, 1]]

shape_list.append(line)

l_shape = [[1, 0],
           [1, 0],
           [1, 1]]

shape_list.append(l_shape)

reverse_l_shape = [[0, 1],
                   [0, 1],
                   [1, 1]]

shape_list.append(reverse_l_shape)

t_shape = [[1, 1, 1],
           [0, 1, 0]]

shape_list.append(t_shape)

z_shape = [[1, 1, 0],
           [0, 1, 1]]

shape_list.append(z_shape)

reverse_z_shape = [[0, 1, 1],
                   [1, 1, 0]]

shape_list.append(reverse_z_shape)


# Create the Tetromino class
class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = ("white", "yellow", "magenta", "red", "cyan", "green", "blue")[shape_list.index(shape)]
        self.draw()

    def draw(self):
        turtle.tracer(0)
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        for row in self.shape:
            for block in row:
                if block:
                    turtle.begin_fill()
                    for _ in range(4):
                        turtle.forward(20)
                        turtle.left(90)
                    turtle.end_fill()
                    turtle.forward(20)
                else:
                    turtle.forward(20)
            turtle.penup()
            turtle.goto(self.x, self.y - 20 * self.shape.index(row))
            turtle.pendown()
        turtle.update()

    def move(self, dx, dy):
        self.erase()
        self.x += dx
        self.y += dy
        self.draw()

    def erase(self):
        turtle.color("black")
        for row in self.shape:
            for block in row:
                if block:
                    turtle.begin_fill()
                    for _ in range(4):
                        turtle.forward(20)
                        turtle.left(90)
                    turtle.end_fill()
                    turtle.forward(20)
                else:
                    turtle.forward(20)
            turtle.penup()
            turtle.goto(self.x, self.y - 20 * self.shape.index(row))
            turtle.pendown



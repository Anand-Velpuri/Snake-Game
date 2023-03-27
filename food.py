from turtle import Turtle
import random
food_colors = ["gold", "white", "grey", "olive", "red"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.color_change()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()

    def color_change(self):
        food_color = random.choice(food_colors)
        self.color(food_color)

    def refresh(self):
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)
        self.goto(random_x, random_y)

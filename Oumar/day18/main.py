import turtle as T
from random import choice, randint, random
t = T.Turtle()
T.colormode(255)
# def random_color():
#     r = randint(0, 255)
#     g =randint(0, 255) 
#     b = randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# # num_sides = [3, 4, 5, 6, 7, 8, 9, 10, 11]
# # for _ in range (i in num_sides):
# #     angka = 360 / num_sides[_]
# #     t.forward(100)
# #     t.right(angka)    
# # def draw_shape(num_sides):
# #     angka = 360 / num_sides
# #     for _ in range(num_sides):
# #         t.forward(100)
# #         t.right(angka)

# # for i in num_sides:
# #     t.color(choice(colors))
# #     draw_shape(i)
# # directions= [0, 90, 180, 270]
# # while True:
# #     t.color(random_color())
# #     t.forward(30)
# #     t.setheading(choice(directions))
# #     t.pensize(10)
# #     t.speed(10)
# def draw_spirograph(gap_size):
#     for i in range(int(360/gap_size)):
#         t.speed(100)
#         t.color(random_color())
#         t.dot(20)
#         t.forward(t.heading() + gap_size)

# draw_spirograph(5)

color_list = [(202,164,109),(240,245,249),(236,239,243),(149,75,50),(222,201,136),(53,93,123),(170,154,41),(138,31,20),(134,163,184),(197,92,73),(47,121,86),(85,57,51),(215,153,33),(154,147,149),(106,74,77),(55,46,49)]
t.penup()
t.hideturtle()
# t.setheading(225)
# t.forward(300)
# t.setheading(0)
t.speed("fastest")
number_of_dots = 100

def draw_dots():
    for i in range(1, number_of_dots+1):
        t.dot(20, choice(color_list))
        t.forward(50)
        if i%10 == 0:
            t.setheading(90)
            t.forward(50)
            t.setheading(180)
            t.forward(500)
            t.setheading(0)
        
        
        
        

draw_dots()
screen = T.Screen()
screen.exitonclick()
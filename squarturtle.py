import turtle

def draw_square(side_length):
    t = turtle.Turtle()
    
    for _ in range(4):
        t.forward(side_length)  
        t.right(90)         

    turtle.done()

side_length = int(input("Enter the side length of the square: "))

draw_square(side_length)

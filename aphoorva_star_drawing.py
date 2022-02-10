import turtle

setpositionx =-100
line_length = 100
    
def stars():
    turtle.fillcolor("yellow")
    turtle.begin_fill()
     
    for side in range(5):
        turtle.forward(line_length)
        turtle.right(144)
    turtle.end_fill()
    
for i in range(3):
    turtle.penup()
    turtle.setpos(setpositionx,0)
    turtle.pendown() 
    stars()
    line_length = line_length + 10
    setpositionx =setpositionx + 115
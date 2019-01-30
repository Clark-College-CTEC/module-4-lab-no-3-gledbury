# Lab No. 3
# CTEC 121
# George Ledbury

from graphics import *  

def snowman():
    # create the graphics window
    win = GraphWin('Lab 3 - Snowman',800,800)
    
    # your code to draw the snowman goes here
    # draw three circles for the body
    # name the three circles circle1, circle2 and circl3
    circle1 = Circle(Point(400,200),40)
    circle1.setWidth(3)
    circle1.draw(win)
    circle2 = Circle(Point(400,300),60)
    circle2.setWidth(3)
    circle2.draw(win)
    circle3 = Circle(Point(400,440),80)
    circle3.setWidth(3)
    circle3.draw(win)


    # draw two eyes on the top circle
    # name the two eyes using variables eye1 and eye2
    eye1 = Circle(Point(380,180),5)
    eye1.setFill('black')
    eye1.draw(win)
    eye2 = eye1.clone()
    eye2.move(40,0)
    eye2.draw(win)

    # draw a nose using the polygon method and make it orange
    # name the nose using the variable nose
     
     
    nose = Polygon(Point(390,190),Point(410,190),Point(400,210))
    nose.setFill('orange')

    nose.draw(win)

    # draw a hat using a rectangle and fill it with black
    # name the hat using the variable hat
    hat = Rectangle(Point(380,160), Point(420,120))
    hat.setFill('black')
    hat.draw(win)

    # draw a line to represent the rim of the hat using a line
    # name the line using the variable hatline
    brim = Line(Point(340,160), Point(460,160))
    brim.setWidth('3')
    brim.draw(win)
  

    # close the program
    input('Press enter to quit the program ')
    # close the graphics window
    win.close()


# Call the snowman() function to start the program
snowman()
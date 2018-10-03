import turtle as t
from utils import *
import statistics

def WIDTH():
    """
    function to set length of the x axis
    :return: length of x axis
    """
    return 341.5

def HEIGHT():
    """
    fucntion to set height of the y axis
    :return: height of y axis
    """
    return 288

def MARGIN_WIDTH():
    """
    function to set width margin
    :return: margin
    """

    return 50

def MARGIN_HEIGHT():
    """
    function to set heigth margin
    :return: margin
    """

    return 50

def x_set(value):
    """
    helper function for setting origin
    :param value: given value
    :return: updated value
    """

    temp = (-WIDTH()+MARGIN_WIDTH())-1960
    #print(temp)
    x_length = 2 * WIDTH() - 2 * MARGIN_WIDTH()
    # print(x_length)
    division = 2015 - 1960
    per_div_val = x_length / division
    # print(per_div_val)
    x = 1960 + temp

    return x + (per_div_val*(value-1960))

def y_set(value):
    """
    helper function for setting origin
    :param value: given value
    :return: updated value
    """
    temp = (-HEIGHT()+MARGIN_HEIGHT())
    y_length = 2*(HEIGHT()-MARGIN_HEIGHT())
    division = 90
    per_div_val = y_length / division

    return temp + (per_div_val * (value))


def label():
    """
    labelling of graphs
    :return: None
    """

    values = ["0","10","20","30","40","50","60","70","80","90"]
    j=0
    for i in values:
        t.up()
        t.goto(x_set(1959),y_set(j))
        t.down()
        #print(x_set(1960))
        #print(y_set(10))
        t.write(i,align="left")
        j += 10
        #print(j)

######## second part

    t.up()
    t.goto(x_set(1960),y_set(-5))
    t.write("1960")
    t.goto(x_set(2015),y_set(-5))
    t.write("2015")

############ third part: naming ###################

    t.goto(x_set(1956),y_set(50))
    t.write("Life\nExp.")
    t.goto(x_set(1987.5),y_set(-5))
    t.write("Year")



def label_income():
    """
    labelling function for income graph
    :return: None
    """

    label()
    t.pensize(3)
    colors = ["blue","red","green","orange"]
    t.goto(x_set(1965),y_set(100))
    t.pencolor("blue")
    t.write("Low income")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)

    t.up()
    t.goto(x_set(1965), y_set(95))
    t.pencolor("red")
    t.write("Upper middle income")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)

    t.up()
    t.goto(x_set(1965), y_set(90))
    t.pencolor("green")
    t.write("Lower middle income")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)

    t.up()
    t.goto(x_set(1965), y_set(85))
    t.pencolor("orange")
    t.write("High income")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)


def init_income():
    """
    initialization function for income graph
    :return: None
    """
    t.up()
    t.goto(-WIDTH()+MARGIN_WIDTH(), -HEIGHT()+MARGIN_HEIGHT())
    t.down()
    t.forward(2*WIDTH()-2*MARGIN_WIDTH())
    t.backward(2*WIDTH()-2*MARGIN_WIDTH())
    t.left(90)
    t.forward(2*(HEIGHT()-MARGIN_HEIGHT()))
    t.backward(2*(HEIGHT()-MARGIN_HEIGHT()))
    t.up()
    t.home()
    t.down()
    label_income()


def label_region():
    """
    labelling function for region graph
    :return: None
    """

    label()
    t.pensize(3)
    colors = ["blue", "red", "green", "orange"]
    t.goto(x_set(1965), y_set(100))
    t.pencolor("blue")
    t.write("Sub-Saharan Africa")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)

    t.up()
    t.goto(x_set(1965), y_set(95))
    t.pencolor("red")
    t.write("South Asia")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)

    t.up()
    t.goto(x_set(1965), y_set(90))
    t.pencolor("green")
    t.write("Europe & Central Asia")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)

    t.up()
    t.goto(x_set(1965), y_set(85))
    t.pencolor("black")
    t.write("Middle East & North Africa")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)

    t.up()
    t.goto(x_set(1965), y_set(80))
    t.pencolor("yellow")
    t.write("North America")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)

    t.up()
    t.goto(x_set(1965), y_set(75))
    t.pencolor("purple")
    t.write("East Asia & Pacific")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)

    t.up()
    t.goto(x_set(1985), y_set(85))
    t.pencolor("orange")
    t.write("Latin America & Caribbean")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)


def init_region():
    """
    initialization function for region graph
    :return: None
    """
    t.up()
    t.goto(-WIDTH() + MARGIN_WIDTH(), -HEIGHT() + MARGIN_HEIGHT())
    t.down()
    t.forward(2 * WIDTH() - 2 * MARGIN_WIDTH())
    t.backward(2 * WIDTH() - 2 * MARGIN_WIDTH())
    t.left(90)
    t.forward(2 * (HEIGHT() - MARGIN_HEIGHT()))
    t.backward(2 * (HEIGHT() - MARGIN_HEIGHT()))
    t.up()
    t.home()
    t.down()
    label_region()
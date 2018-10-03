"""
File Name: factors.py
Author's Name: Tejaswini Jagtap
"""

from utils import *
import turtle as t

def get_sorted(data):
    """
    gives the year and its median life expectancy value
    :param data: data containing the information about year, country, life expectancy
    :return: life_expectancy dictionary
    """
    life_expectancy_dic = {}
    year = 1960
    while year != 2016:
        c = []
        l = 0
        for k, v in data.items():
            if v[3][year] != '':
                c.append(v[3][year])
                l += 1
        c.sort()

        if l % 2 == 0 and l!=0:
            a = float(c[(l // 2)-1])
            b = float(c[(l // 2)])
            d = (a + b) / 2
        else:
            d = float(c[(l // 2)-1])
        life_expectancy_dic[year] = d
        year += 1
    return life_expectancy_dic

def init():
    t.reset()
    t.up()

def draw_help1(a, color):
    """
    hepl drawing 1st graph
    :param a: dictionary containing year and its median expectancy
    :param color: color of the pen
    :return: graph
    """

    for k, v in a.items():
            r=k-1960
            u = r*10
            q = v*5
            t.down()
            t.goto(-170+u, -170+q)
            t.pencolor(color)

    t.pencolor("black")
    t.up()
    t.goto(-170, -170)




def naming1():
    """
    names the graph
    """
    t.up()
    t.right(90)
    t.right(90)
    t.forward(18)
    t.down()
    t.left(90)
    t.write("1960")
    t.up()
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward((55*10)/2)
    t.down()
    t.write("Year")
    t.up()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(55*10/2)
    t.down()
    t.write("2015")
    t.up()
    t.back(((55*10)) +18 )
    t.left(90)
    t.forward(14)
    t.right(90)
    t.down()
    t.write("0")
    hp("10")
    hp("20")
    hp("30")
    hp("40")
    hp("50")
    hp("60")
    hp("70")
    hp("80")
    hp("90")
    t.up()
    t.back(50)
    t.right(90)
    t.forward(9*50/2)
    t.left(90)
    t.down()
    t.write("Life Exp.")
    t.up()
    t.pensize(3)
    t.goto(-170 + 700, -170 + 30)
    t.pencolor("blue")
    t.write("Low income")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)
    t.up()
    t.goto(-170 + 650, -170 + 30)
    t.pencolor("red")
    t.write("Upper middle income")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)
    t.up()
    t.goto(-170 + 600, -170 + 30)
    t.pencolor("green")
    t.write("Lower middle income")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)
    t.up()
    t.goto(-170 + 550, -170 + 30)
    t.pencolor("orange")
    t.write("High income")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)

def naming2():
    """
    names the graph
    """
    t.up()
    t.right(90)
    t.right(90)
    t.forward(18)
    t.down()
    t.left(90)
    t.write("1960")
    t.up()
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward((55*10)/2)
    t.down()
    t.write("Year")
    t.up()
    t.left(90)
    t.forward(20)
    t.right(90)
    t.forward(55*10/2)
    t.down()
    t.write("2015")
    t.up()
    t.back(((55*10)) +18 )
    t.left(90)
    t.forward(14)
    t.right(90)
    t.down()
    t.write("0")
    hp("10")
    hp("20")
    hp("30")
    hp("40")
    hp("50")
    hp("60")
    hp("70")
    hp("80")
    hp("90")
    t.up()
    t.back(50)
    t.right(90)
    t.forward(9*50/2)
    t.left(90)
    t.down()
    t.write("Life Exp.")
    t.up()
    t.pensize(3)
    t.goto(-170 + 700, -170 + 30)
    t.pencolor("blue")
    t.write("Sub-Saharan Africa")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)
    t.up()
    t.goto(-170 + 650, -170 + 30)
    t.pencolor("red")
    t.write("South Asia")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)
    t.up()
    t.goto(-170 + 600, -170 + 30)
    t.pencolor("green")
    t.write("Europe & Central Asia")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)
    t.up()
    t.goto(-170 + 550, -170 + 30)
    t.pencolor("black")
    t.write("Middle East & North Africa")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)
    t.up()
    t.goto(-170 + 500, -170 + 30)
    t.pencolor("yellow")
    t.write("North America")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)
    t.up()
    t.goto(-170 + 450, -170 + 30)
    t.pencolor("purple")
    t.write("East Asia & Pacific")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)
    t.up()
    t.goto(-170 + 400, -170 + 30)
    t.pencolor("orange")
    t.write("Latin America & Caribbean")
    t.left(90)
    t.forward(8)
    t.right(90)
    t.forward(130)
    t.down()
    t.forward(30)


def hp(p):
    """
    helps to draw the graph
    :param p: to be printed
    """
    t.up()
    t.left(90)
    t.forward(50)
    t.down()
    t.right(90)
    t.write(p)


def draw_graph1(a,b,c,d):
    """
    draws the graph
    :param a: dictionary containing year and its median expectancy
    :param b: dictionary containing year and its median expectancy
    :param c: dictionary containing year and its median expectancy
    :param d: dictionary containing year and its median expectancy
    :return: graph
    """
    t.up()
    t.setpos(-170, -170)
    t.down()
    t.forward(55*10)
    t.back(55*10)
    t.left(90)
    t.forward(9*50)
    t.back(9*50)
    draw_help1(a, "blue")
    draw_help1(b, "red")
    draw_help1(c, "green")
    draw_help1(d, "orange")


def draw_graph2(e, f, g, h, i, j, k):
    """
        draws the graph
        :param e: dictionary containing year and its median expectancy
        :param f: dictionary containing year and its median expectancy
        :param g: dictionary containing year and its median expectancy
        :param h: dictionary containing year and its median expectancy
        :param i: dictionary containing year and its median expectancy
        :param j: dictionary containing year and its median expectancy
        :param k: dictionary containing year and its median expectancy
        :return: graph
        """
    t.up()
    t.setpos(-170, -170)
    t.down()
    t.forward(55 * 10)
    t.back(55 * 10)
    t.left(90)
    t.forward(9 * 50)
    t.back(9 * 50)
    draw_help1(e, "blue")
    draw_help1(f, "red")
    draw_help1(g, "green")
    draw_help1(h, "orange")
    draw_help1(i, "black")
    draw_help1(j, "yellow")
    draw_help1(k, "purple")
    #naming()



def main():
    """
    draws the graph of all the datas of year and life expectancies
    """
    (entries, larger, meta, data, reg, inc) = read_data('worldbank_life_expectancy')
    inc_data1 = filter_income(data, "Low income")
    inc_data2 = filter_income(data, "Upper middle income")
    inc_data3 = filter_income(data, "Lower middle income")
    inc_data4 = filter_income(data, "High income")

    a = get_sorted(inc_data1)
    b = (get_sorted(inc_data2))
    c = (get_sorted(inc_data3))
    d = (get_sorted(inc_data4))

    reg_data1 = filter_region(data, "Sub-Saharan Africa")
    reg_data2 = filter_region(data, "South Asia")
    reg_data3 = filter_region(data, "Europe & Central Asia")
    reg_data4 = filter_region(data, "Latin America & Caribbean")
    reg_data5 = filter_region(data, "Middle East & North Africa")
    reg_data6 = filter_region(data, "North America")
    reg_data7 = filter_region(data, "East Asia & Pacific")

    e = (get_sorted(reg_data1))
    f = (get_sorted(reg_data2))
    g = (get_sorted(reg_data3))
    h = (get_sorted(reg_data4))
    i = (get_sorted(reg_data5))
    j = (get_sorted(reg_data6))
    k = (get_sorted(reg_data7))

    draw_graph1(a, b, c, d)
    naming1()
    get = input("Hit enter for the next graph")
    if get == "":
        t.reset()
    draw_graph2(e, f, g, h, i, j, k)
    naming2()



if __name__=='__main__':
    main()
    t.mainloop()
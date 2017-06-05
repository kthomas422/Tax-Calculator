#-----------------------------------------------------------------------
# Author: Kyle Thomas
# My python program for calculating taxes and room charges for a hotel
# This program requires the Zelle Graphics Library which can be found at
# http://mcsp.wartburg.edu/zelle/python/
#-----------------------------------------------------------------------


from graphics import Entry, Image, GraphWin, Point, Rectangle, Text


# Tax Rates:
TAX_RATE = 1.103      # 1 + 8.3% sales + 2% occupancy tax
FLAT_TAX = 2          # $2 per night city/county tax


# Purpose: To calculate the total charges after tax
#   Input: The room rate (float)
#  Output: The total after tax (float)
def calc_tax(rate):
    return rate * TAX_RATE + FLAT_TAX


# Purpose: To calculate just the room charges without tax
#   Input: The number of nights (int) and the total charges (float)
#  Output: The total room charges (minus tax) (float)
def calc_rate(nights, total):
    return ((total / nights) - FLAT_TAX) / TAX_RATE


# Purpose: To calculate the total tax paid
#   Input: The rate (float), the total and the number of nights (int)
#  Output: The tax paid (float)
def calc_diff(rate, total, nights):
    return total - (rate * nights)


# Purpose: To determine whether a point is in a rectangle or not
#   Input: A rectangle and a point
#  Output: A True or False whether the point is in the rectangle or not
def is_pt_in_rect(rectangle, point):
    point1 = rectangle.getP1()
    point1X = point1.getX()
    point1Y = point1.getY()
    point2 = rectangle.getP2()
    point2X = point2.getX()
    point2Y = point2.getY()
    sideOneLength = abs(point1X - point2X)
    sideTwoLength = abs(point1Y - point2Y)
    pointXvalue = point.getX()
    pointYvalue = point.getY()

    if ((abs(point1X - pointXvalue) <= sideOneLength
        and abs(point2X - pointXvalue) <= sideOneLength)
        and (abs(point1Y - pointYvalue) <= sideTwoLength
        and abs(point2Y - pointYvalue) <= sideTwoLength)):

        inFlag = True

    else:
        inFlag = False

    return inFlag


def main():
    window = GraphWin("Tax Calculator", 300, 350)
    window.setBackground("White")

    banner = Text(Point(150, 20), "Tax Calculator")
    banner.setStyle("bold")
    banner.setFace("courier")
    banner.setSize(18)
    banner.draw(window)

    rateText = Text(Point(60,80), "Rate:")
    rateText.setFace("courier")
    rateText.draw(window)

    rateBox = Entry(Point(200, 80), 7)
    rateBox.setFill("White")
    rateBox.setText("0")
    rateBox.draw(window)

    nightText = Text(Point(50, 140), "Nights:")
    nightText.setFace("courier")
    nightText.draw(window)

    nightBox = Entry(Point(200, 140), 7)
    nightBox.setFill("White")
    nightBox.setText("1")
    nightBox.draw(window)

    totalText = Text(Point(56, 200), "Total:")
    totalText.setFace("courier")
    totalText.draw(window)

    totalBox = Entry(Point(200, 200), 7)
    totalBox.setFill("White")
    totalBox.setText("0")
    totalBox.draw(window)

    calc = Image(Point(150, 310), "button.png")
    calc.draw(window)

    calcButton = Rectangle(Point(68,288), Point(232, 332))

    calcFlag = False  # Flag of whether or not a calculation has been performed

    while True:
        errorFlag = False
        try:
            mouseClick = window.getMouse()

        except:
            window.close()
            break

        if (is_pt_in_rect(calcButton, mouseClick)):
            try:
                rate = float(rateBox.getText())
                nights = int(nightBox.getText())
                total = float(totalBox.getText())

            except:  # Reset boxes and clear totals
                totalBox.setText("0")
                nightBox.setText("1")
                rateBox.setText("0")
                if calcFlag:
                    totalTax.undraw()
                    nightlyTax.undraw()

                errorFlag = True

            # Make sure values are "sane"
            if ((not errorFlag) and (rate < 0 or nights < 1 or total < 0)):
                totalBox.setText("0")
                nightBox.setText("1")
                rateBox.setText("0")
                if calcFlag:
                    totalTax.undraw()
                    nightlyTax.undraw()
                errorFlag = True

            if (not errorFlag):
                if (rate > 0):
                    total = round(calc_tax(rate) * nights, 2)
                    totalBox.setText(str(total))
                    if calcFlag:
                        totalTax.undraw()
                        nightlyTax.undraw()

                    nightlyTax = Text(Point(150, 245),
                                 "Nightly Tax: "
                                 + str(round(calc_tax(rate) - rate, 2)))

                    nightlyTax.setFill("red")
                    nightlyTax.setFace("courier")
                    nightlyTax.draw(window)

                    totalTax = Text(Point(150, 270),
                                 "Total Tax: "
                                 + str(round(
                                     calc_diff(rate, total, nights), 2)))

                    totalTax.setFill("red")
                    totalTax.setFace("courier")
                    totalTax.draw(window)

                    calcFlag = True

                elif (total > 0):
                    rate = round(calc_rate(nights, total), 2)
                    rateBox.setText(str(rate))
                    if calcFlag:
                        totalTax.undraw()
                        nightlyTax.undraw()

                    nightlyTax = Text(Point(150, 245),
                                 "Nightly Tax: "
                                 + str(round(calc_tax(rate) - rate, 2)))

                    nightlyTax.setFill("red")
                    nightlyTax.setFace("courier")
                    nightlyTax.draw(window)

                    totalTax = Text(Point(150, 270),
                                 "Total Tax: "
                                 + str(round(
                                     calc_diff(rate, total, nights), 2)))

                    totalTax.setFill("red")
                    totalTax.setFace("courier")
                    totalTax.draw(window)

                    calcFlag = True
    return
main()

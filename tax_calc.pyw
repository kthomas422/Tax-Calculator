#-------------------------------------------------------------------------------
# Author: Kyle Thomas
# My python program for calculating taxes and room charges for a hotel
# This program requires Zelle Graphics Library which can be downloaded from
# http://mcsp.wartburg.edu/zelle/python/
#-------------------------------------------------------------------------------

from graphics import *


# Tax Rates:
#===================================================================
tax_rate = 1.103      # 1 + 8.3% sales + 2% occupancy tax
flat_tax = 2          # $2 per night city/county tax
#===================================================================


# Purpose: To calculate the total charges after tax
#   Input: The number of nights to stay and the rate
#  Output: The total charges after tax
def calcTax(nights, rate):
    return round(nights * (tax_rate * rate + flat_tax), 2)

# Purpose: To calculate just the room charges without tax
#   Input: The number of nights and the total charges
#  Output: The total room charges (minus tax) and the rate per night
def calcRate(nights, total):
    return round((((total / nights) - flat_tax) / tax_rate), 2)

# Purpose: To calculate the total tax paid
#   Input: The rate, the total and the number of nights
#  Output: The tax paid
def calcDiff(rate, total, nights):
    return round(total - (rate * nights), 2)

# Purpose: To calculate the nightly tax paid
#   Input: The rate, the total and the number of nights
#  Output: The nightly tax paid
def calcNightlyTax(rate):
    return round(calcTax(1,rate) - rate, 2)

# Purpose: To determine whether a point is in a rectangle or not
#   Input: A rectangle and a point
#  Output: A True or False whether the point is in the rectangle or not
def isPtInRect(rectangle, point):
    point1 = rectangle.getP1()      # First rectangle point
    point1X = point1.getX()         # First rectangle point X coord
    point1Y = point1.getY()         # First rectangle point Y coord
    point2 = rectangle.getP2()      # Second rectangle point
    point2X = point2.getX()         # Second rectangle point X coord
    point2Y = point2.getY()         # Second rectangle point Y coord
    sideOneLength = abs(point1X - point2X)
    sideTwoLength = abs(point1Y - point2Y)
    pointXvalue = point.getX()      # Input point X coord
    pointYvalue = point.getY()      # Input point Y coord
    if (abs(point1X - pointXvalue) <= sideOneLength and \
        abs(point2X - pointXvalue) <= sideOneLength) and \
        (abs(point1Y - pointYvalue) <= sideTwoLength and \
         abs(point2Y - pointYvalue) <= sideTwoLength):

        inFlag = True

    else:
        inFlag = False
    
    return inFlag

def main():

    #---------------------
    # Initializing window
    #---------------------
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

    calcFlag = False # Flag of whether or not a calculation has been performed

    while True:
        errorFlag = False
        try:
            click = window.getMouse()

        except:
            window.close()
            break

        if(isPtInRect(calcButton, click)):
            try:
                rate = float(rateBox.getText())
                nights = int(nightBox.getText())
                total = float(totalBox.getText())

            except: # Reset boxes and clear totals
                totalBox.setText("0")
                nightBox.setText("1")
                rateBox.setText("0")
                if calcFlag:
                    diff0.undraw()
                    diff1.undraw()
                errorFlag = True

            # Make sure values are "sane"
            if ((not errorFlag) and (rate < 0 or nights < 0 or total < 0)):
                totalBox.setText("0")
                nightBox.setText("1")
                rateBox.setText("0")
                if calcFlag:
                    diff0.undraw()
                    diff1.undraw()
                errorFlag = True

            if (not errorFlag):
                if(rate > 0):
                    total = calcTax(nights, rate)
                    totalBox.setText(str(total))
                    if calcFlag:
                        diff0.undraw()
                        diff1.undraw()
                    diff0 = Text(Point(150, 270),
                                 "Total Tax: " + str(calcDiff(rate, total, nights)))

                    diff0.setFill("red")
                    diff0.setFace("courier")
                    diff0.draw(window)

                    diff1 = Text(Point(150, 245),
                                 "Nightly Tax: " + str(calcNightlyTax(rate)))
                    
                    diff1.setFill("red")
                    diff1.setFace("courier")
                    diff1.draw(window)
                    
                    calcFlag = True

                elif(total > 0):
                    rate = calcRate(nights, total)
                    rateBox.setText(str(rate))
                    if calcFlag:
                        diff0.undraw()
                        diff1.undraw()

                    diff0 = Text(Point(150, 270),
                                 "Total Tax: " + str(calcDiff(rate, total, nights)))
                    
                    diff0.setFill("red")
                    diff0.setFace("courier")
                    diff0.draw(window)

                    diff1 = Text(Point(150, 245),
                                 "Nightly Tax: " + str(calcNightlyTax(rate)))
                    
                    diff1.setFill("red")
                    diff1.setFace("courier")
                    diff1.draw(window)

                    calcFlag = True
    return

main()

#=============
# End of file
#=============

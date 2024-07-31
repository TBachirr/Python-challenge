def paintcalculator(width,height):
    numberofcan = (width*height)/5
    can = round(numberofcan)
    print("The number of cans needed is ",can)
w = int(input("Enter the width "))
h = int(input("Enter the height "))
paintcalculator(w,h)
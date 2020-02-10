#Title: Calculates the total cost of an item with GST and PST in BC
price = float(input("Enter the cost of this item without tax included:"))
GST = price * 0.05 #GST rate in 2020 = 5%
PST = price * 0.07 #PST rate in 2020 = 7%
tax= GST + PST
total = price + tax
#round() rounds the number
print("The total cost of this item including tax is" + " $" + str(round(total,2))) #The ",2" at the end of "total", rounds the number to 2 decimal places
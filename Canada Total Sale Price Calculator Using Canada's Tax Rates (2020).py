#Title: Calculates the total cost of an item using Canada's tax rates from 2020
print("Use the number within the brackets when selecting your location, British Columbia[1], Alberta [2], Saskatchewan[3],\n "
      "Manitoba[4], Ontario[5], Quebec[6], New Brunswick[7], Nova Scotia[8], Prince Edward Island[9],"
      " Newfoundland and Labrador[10], \nYukon[11], Northwest Territories[12], Nunavut[13]")
area=eval(input("Please select your location by typing the number inside the bracket:"))
if area== 1: #British Columbia
    print("The location you selected is British Columbia")
    GST = 0.05 #GST rate in 2020 = 5%
    PST = 0.07 #PST rate in 2020 = 7%
    HST = 0   #This area has no HST
elif area== 2: #Alberta
    print("The location you selected is Alberta")
    GST = 0.05  # GST rate in 2020 = 5%
    PST = 0 #Alberta does not have PST
    HST = 0  # This area has no HST
elif area== 3: #Saskatchewan
    print("The location you selected is Saskatchewan")
    GST= 0.05
    PST= 0.06
    HST = 0  # This area has no HST
elif area== 4: #Manitoba
    print("The location you selected is Manitoba")
    GST = 0.05
    PST = 0.07
    HST = 0  # This area has no HST
elif area== 5: #Ontario
    print("The location you selected is Ontario")
    GST = 0
    PST = 0
    HST = 0.13
elif area== 6:
    print("The location you selected is Quebec")
    GST = 0.05
    PST = 0.09975
    HST = 0  # This area has no HST
elif area== 7: #New Brunswick
    print("The location you selected is New Brunswick")
    GST = 0
    PST = 0
    HST = 0.15
elif area== 8: #Nova Scotia
    print("The location you selected is Nova Scotia")
    GST = 0
    PST = 0
    HST = 0.15
elif area== 9: #Prince Edward Island
    print("The location you selected is Prince Edward Island")
    GST = 0
    PST = 0
    HST = 0.15
elif area== 10: #Newfoundland and Labrador
    print("The location you selected is Newfoundland and Labrador")
    GST = 0
    PST = 0
    HST = 0.15
elif area== 11: #Yukon
    print("The location you selected is Yukon")
    GST = 0.05
    PST = 0
    HST = 0  # This area has no HST
elif area== 12: #Northwest Territories
    print("The location you selected is Northwest Territories")
    GST = 0.05
    PST = 0
    HST = 0  # This area has no HST
elif area== 13: #Nunavut
    print("The location you selected is Nunavut")
    GST = 0.05
    PST = 0
    HST = 0  # This area has no HST
else:
    print("Please restart this program and select a valid country")
    exit()
price = float(input("Enter the cost of the item without tax and the \"$\" symbol included:"))
if price<0:
    print("Please restart this program and select a valid price")
    exit()
else:
    tax= (GST * price) + (PST * price) + (HST * price)
    total = price + tax
    #round() rounds the number
    print("The total cost of this item including tax is" + " $" + str(round(total,2))) #The ",2" at the end of "total", rounds the number to 2 decimal places
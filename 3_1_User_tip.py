#Allows a user to choose how much they would like to tip


bill = input("Enter your bill: ")

userTip = input("Enter how much percent you would like to tip: ")

tip = (bill / 100.0) * userTip

total = bill + tip

print "The tip on a £", bill, "meal at ", userTip, "%% is: £%0.2f"% (tip)
 

print "the total for this meal is: £%0.2f" % (total) 


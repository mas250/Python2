#order t-shirts with free delivery

print ("Welcome to MatStore /n T-Shirts are £15")
shirts = input("How many shirts would you like?")
total = (shirts * 15)+ 5
if shirts >= 10:
    print "This order qualifies for free delivery"
    discount = (shirts * 12)
    print discount


else :
    print "The total cost of delivers: £", total
            


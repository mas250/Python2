#VAT Calculator

print " This program will prompt yuou to input the ex VAT amount (in £), then"

print "output the total amount inclusive of VAT"
print
VATPERCENT = 15.0

amount = input ("Enter the ex VAT amount in £: ")
vat = amount *VATPERCENT /100.0
totalAmount = amount + vat
print
print "The total ammount (inclusive of VAT) is £",totalAmount
print

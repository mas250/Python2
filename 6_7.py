# -*- coding: cp1252 -*-
print "This program will tell you how many years it will take for an"
print "Inital investment of £500 to reach £1000 if the intrest rate is 6%\n"

balance = input("how much would you like to invest with Mat-Bank?:  ")

years = 0

while balance < 1000:
    intrest = balance * 6/100.0
    balance = balance + intrest
    years = years + 1
print "It will take", years, "years for your investment to reach £1000"

# -*- coding: cp1252 -*-
print "This program will tell you how many years it will take for the"
print "population of Uganda to exceed 50 Million \n"

population = 26000000

years = 0

while population < 50000000:
    growth = population * 6/100.0
    population = population + growth
    years = years + 1
print "It will take", years, "years for the population of Uganda to reach 50 Million."

# tempConvertWarning2.py
# A temperature conversion program using an if...else structure to output
# a weather warning
# written by D.H.,December 2,2004

print "This program will ask you to input the temperature in degrees Fahrenheit"
print "then output the equivalent temperature in degrees Centigrade."
print "The program will issue appropriate weather warnings for extreme"
print "temperatures."
print

fahrenheit = input ("Enter the temperature in degrees Fahrenheit: ")
centigrade =  (fahrenheit - 32)* 5/9.0

print "The equivalent temperature in degrees Centigrade is %0.0f" % centigrade
print

# check if weather warning needed
if centigrade <= 0:
    print "It's freezing. Best to wear a thick coat today."
    print "dont forget to wear a scarf!"
    print "Or maybe you shold stay in bed"
    print " Comouters care not for cold"
elif centigrade >= 30:
    print " Its to hot stay inside and play games"

else:
    print "There are no extreme weather warnings today."
    print " the internet has no weather"
   
print "Have a pleasant day."

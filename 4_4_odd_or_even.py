# odd_or_even.py
# A program to determine if a whole number input from the keyboard
# is odd or even.
# written by D.H.,December 1, 2004

number = input( "Type in a whole number: ")
print
remainder = number % 2
factor3 = number % 3
if remainder == 0:
    print "Your number is even"
if  factor3 == 0:
    print "Your number is divisible by 3"
else:
    print "Your number is odd"

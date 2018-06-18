#validate.py
#Program prompts user to enter an integer between 5 and 10 (inclusive) until
#they do so correctly.
#Written by P.K., January 24th 2005

number = input("Enter an integer between 5 and 10 (inclusive): ")

while number >10 or number < 5:
    print "Invalid input!",
    number = input("Enter an integer between 5 and 10 (inclusive): ") 

print "Thank-you!"

from random import randrange

number = randrange(1,101)

print "Guess the mystery number - it's between 1 a 100!"
guess = input("Type in you first guess:   ")
while guess != number:

    if guess > number:
        print "Too high! Guess Lower!"
    else:
        print "Too Low! Guess Higher!"
    guess = input("Type in your guess:  ")

print "Well done. You are right!"
print "The number was", number
            

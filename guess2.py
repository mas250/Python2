from random import randrange

number = randrange(1,101)

print "Guess the mystery number - it's between 1 and 100!"
guess = input("Type in your first guess:  ")
guessCount = 1
while guess != number:
    if guess > number:
        print "Too high! Guess Lower!"
    else:
         print "Too low! Guess higher!"
    guess = input("Guess again!   ")
    guessCount = guessCount+1

print "Well done. You are right!"
print "The number was", number
print "You guessed the number in", guessCount, "guesses."

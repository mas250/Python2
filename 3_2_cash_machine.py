#efficent cash point gives you the least ammount of notes


money = input ("How much would you like to withdraw? £")

fiftyNote = money / 50

twentyNote = (money - (fiftyNote * 50)) /20

tenNote =(money - ( (fiftyNote * 50) + (twentyNote * 20))  ) /10

fiveNote = (money - ( (fiftyNote * 50) + (twentyNote * 20) + (tenNote * 10) ) ) /5

pounds = money - ( (fiftyNote * 50) + (twentyNote * 20) + (tenNote * 10) +( fiveNote * 5) )

print fiftyNote,"Fifty Pound note(s)"
print twentyNote, "Twenty Pound note(s)"
print tenNote, "Ten Pound note(s)"
print fiveNote, "Five pound note(s)"
print pounds, "Pound coin(s)"

#convert seconds to hours and minutes


time = input("enter the ammount of seconds: ")

hours = (time / 60) / 60
#hourRem = hours%60

minutes = (time /60 ) %60                     #burn the midnight oil
#minutesRem = hourRem % 60

seconds = minutes / 60


print "that is ", hours, " hours, ",  minutes, " minutes", seconds, " seconds "

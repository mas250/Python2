#password.py
#uses a while loop to ensure password is entered correctly

print "Please enter the password.",
password = raw_input("...")

while password != "python":
    print "Enter the password!",
    password = raw_input("...")

print "Paasowrd Accepted"

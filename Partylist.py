#PartyList.py

print "\t\tThis program allows you to maintain"
print "t\t\a list of names opf people to invite"
print "\t\tto a party\n"

names = []          # Creat an empty list

choice = "z"        #Initalize choice with value to set while loop to true

while choice != "q":
    print """
    Choose what you would like to do from the following menu (or q to exit)"

    a: Add a name

    b: Remove a name

    c: Display the names invited

    d: Sort the names alphabetically

    e: Display the number of people invited

    q: quit the program

    """
    choice = raw_input("\nType in your choice (a,b,c,d,e (or q to exit): ")

    
    
    #add a new name
    if choice == "a":
        newName = raw_input("\nEnter a name to add to the party list: ")
        names.append(newName)

    #remove a name
    elif choice == "b":
        oldName = raw_input("\nEnter the name you wish to remove:")
        names.append(newName)
        if oldname in names:
            names.remove(oldName)
        else:
            print
            print oldname,"is not on the guest list"


    #display those invited

    elif choice == "c":
        print "\nYou have invited"
        for i in names:
            print i

    #sort the names alphabetically
    elif choice == "d":
        names.sort()
                
    #use the function len to calculate the number of people invited
    elif choice == "e":
         numberOfPeople = len(names)
         if numberOfPeople == 0:
            print "n\You have invited no one..."
         elif numberOfPeople == 1:
             print "\nYou have invited",  numberOfPeople, "person"
         else:
            print "\n You have invited", numberOfPeople, "people"

    elif choice == "q":
         print "\nGoodbye!"
    else: # if user chose some crazy input
                print "\n Sorry, there was an error in your input"
                print " Valid choices are a,b,c,d or e"
                print "to quit: type q"

           
            

    

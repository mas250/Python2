#5_1. factor.py
factor = input("Enter a number to see its factors: ")

factor_loop = factor+1
                            #make the loop one longer to include
                                # itself as a factor
print
print
print "The factors of", factor, "are:"

for i in range (1, factor_loop):
    
     if factor % i == 0:
         print i,

        
  

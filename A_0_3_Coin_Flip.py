#Author: TEJA SUDHASHREE DEVAGUPTAPU
#Date: 27-01-2025
#A.0.3: Coin Flip - 3 same flips (loop)

import random
i=0
j=0
flips=0
output=[]
def flip_coin():   # Function to define heads or tails during flipping a coin
    if random.binomialvariate(n=1, p=0.5)==1:  # using binominalvariate with 50% probability we return heads or tails.
        return 'H'
    else:
        return 'T'
while i<3 and j<3:  # This will run until we get 3 consecutive heads or tails.

    if flip_coin()=='H': # Calling flip_coin and checking the value returned.
        i=i+1      # increments the i value if its heads.
        j=0     # reset the j value to 0 when its not tails.
        print('H',end=" ")

    else:
        j=j+1   # increments the j value if its tails
        i=0   # reset the i value to 0 when its not heads.
        print('T',end=" ")

    flips=flips+1 # counts the number of flips for each loop until we get 3 heads or tails


print ("(",flips,"flips )")

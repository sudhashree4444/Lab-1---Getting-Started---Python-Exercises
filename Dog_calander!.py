#This Python script calculates the dog years by taking human years as an input
#Author: TEJA SUDHASHREE DEVAGUPTAPU
#Date: 23-01-2025
# A.0.2: DogYears!

human_years  = int(input('enter the human years: ' ))
dog_years = 0
if human_years < 0:
    print('error')
elif human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = 21 + (human_years -2) * 4
print(f'dog years = {dog_years}')




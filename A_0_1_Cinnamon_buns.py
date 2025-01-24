#This Python script solves the Cinnamon buns pricing with discount
#Author: TEJA SUDHASHREE DEVAGUPTAPU
#Date: 23-01-2025
# A.0.1: Cinnamon buns

regular_price = 35.00
discounted_rate = 60
number_of_kanekbulle_ordered = int(input("number of kanebulle purchased:"  ))

regular_price =  regular_price * number_of_kanekbulle_ordered
discount_price = regular_price * (discounted_rate/100)
total_price = regular_price - discount_price

print(f"regular price: {regular_price:.2f} SEK")
print(f"discount price: {discount_price:.2f} SEK")
print(f"total price: {total_price:.2f} SEK")

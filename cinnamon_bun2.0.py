regular_price = 35.00
day_old_cinnamon_bun_discount = 60.00
number_of_cinnamon_bun_ordered = int(input("enter the number of cinnamon buns: " ))

regular_price =  number_of_cinnamon_bun_ordered * regular_price
discount_price = regular_price - day_old_cinnamon_bun_discount
final_price =    number_of_cinnamon_bun_ordered - discount_price

print(f'regular price:  {regular_price:.2f}SEK')
print(f'discount price: {discount_price:.2f}SEK')
print(f'final price:    {final_price:.2f}SEK')
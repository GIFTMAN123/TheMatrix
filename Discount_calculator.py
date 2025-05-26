# Python program to calculate discount for certain goods bought
print("Python program to calculate discounts")
print("=====================================")
Price_of_goods = float(input("Enter the price of goods: "))
Discount_percentage = int(input("Enter the discount percentage(Don''t put '%' at the end): "))
discount = Price_of_goods * Discount_percentage / 100
print("The discount is: " + str(discount))
final_price = Price_of_goods - discount
print("The final price is " + str(final_price))
print("Thank you for using my calculator :D")

# Programmed by Matrix 2025

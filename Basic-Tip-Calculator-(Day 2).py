## Made by @VeritasViso on 19/04/2026 at 12:42pm.

# Basic Tip Calculator (Day 2 of 100)

print("Welcome to the tip calculator!") ## Print the message

total_bill = float(input("What was the total bill? £")) ## Value as an integer/float.
tip = int(input("How much tip would you like to give? 10, 12 or 15?")) ## Value as an integer

final_tip = tip / 100 + 1 ## tip calculation
final_bill = total_bill * final_tip ## final bill before splitting

people_splitting = int(input("How many people split the bill? ")) ## finding out how many people split the bill, and storing it as an integer.
final_amount_per_person = final_bill / people_splitting

print(f"Each person should pay: £{final_amount_per_person:.2f}")

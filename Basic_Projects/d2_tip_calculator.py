#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")
bill_as_float = float(bill)
tip_as_int = int(tip)
people_as_int = int(people)
total_bill = bill_as_float + (bill_as_float * (tip_as_int / 100))
bill_per_person = total_bill / people_as_int
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")

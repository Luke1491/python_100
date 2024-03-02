print("Welcome to the tip calculator.")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
if tip not in [10,12,15]:
    print("Please enter a valid tip percentage.")
    while tip not in [10,12,15]:
        tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))

people=int(input("How many people to split the bill? "))
if people<1:
    print("Please enter a valid number of people.")
    while people<1:
        people=int(input("How many people to split the bill? "))
        
tip_as_percentage=tip/100
total_tip=bill*tip_as_percentage
total_bill=bill+total_tip
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")
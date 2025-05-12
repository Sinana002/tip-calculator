print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $"))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
perc_tip=float((tip/100)*total_bill)
people=int(input("How many people to split the bill?"))
split=(total_bill+perc_tip)/people
split_rounded=round(split,2)
print(f"Each person should pay: ${split_rounded}")

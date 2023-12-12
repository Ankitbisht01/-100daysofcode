
bill_amount = float(input("Please enter total bill amount?"))
no_of_persons = int(input("Please enter number of persons this bill is going to divide"))
tip_percent = int(input("what percent of bill amount you would like to give as tip? 12%, 15% or 20%"))

total_tip = (bill_amount * tip_percent)/100
tip_perperson = total_tip/no_of_persons

print(total_tip)
print("Would you rather have a million dollars or a penny that doubles in value daily for 30 days? (Customizable)")
print()
amnt = float(input("Enter dollar amount to double daily:"))
daystotal = int(input("Enter number of days:"))
day = 1
while day < daystotal:
    amnt=amnt*2
    day=day+1
print("Value after " + str(daystotal) + " days: $" + str(amnt))


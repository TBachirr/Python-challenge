total = input("Enter your total bill amount: ")
persons = float(input("Enter the number of people: "))
tip = input("Enter your tip percentage: ")
tip = float(tip)/100
total = float(total)
tip = total*tip
print(f"Each person should pay: {(total+tip)/persons}")


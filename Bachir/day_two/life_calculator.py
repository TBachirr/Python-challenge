age = input("Enter your age : ")

age_as_int = int (age)
years_remainig = 90 - age_as_int
days_remaining = years_remainig * 365
weeks_remaining = years_remainig * 52
months_remaining = years_remainig * 12

print(f"You have {days_remaining} days, {weeks_remaining}, {months_remaining} remaining")
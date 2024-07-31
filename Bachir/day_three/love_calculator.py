print("Welcome to the love calculator")

name1 = input("What is your name ? \n")
name2 = input("What is their name ? \n")

combined_name = name1 + name2
lower_case = combined_name.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")

true = t + r + u + e

l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, You go together like Code and Mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your love score is {love_score}, You are alright together.")
else: 
    print(f"Your score is {love_score}")



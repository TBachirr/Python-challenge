name = input("What is your name? \n")
love = input("What is your love name? \n")

love_name = name + love
love_name = love_name.lower()

t = love_name.count("t")
r = love_name.count("r")
u = love_name.count("u")
e = love_name.count("e")
l = love_name.count("l")
o = love_name.count("o")
v = love_name.count("v")

true = t + r + u + e 
l = love_name.count("l")
o = love_name.count("o")
v = love_name.count("v")
e = love_name.count("e")
love = l + o + v + e
score = int(str(true) + str(love))
if score < 10 or true > 90:
    print(f"Your love score is {score}, you go together like coke and mentos.")
elif score >= 40 and true <= 50:
    print(f"Your love score is {score}, you are alright together.")
else:
    print(f"Your love score is {score}.")





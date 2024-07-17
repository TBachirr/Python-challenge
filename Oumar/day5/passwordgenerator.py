import random as r
print("Welcome to the PyPassword Generator!")
n = int(input("How many letters would you like in your password?"))
symbols = int(input("How many symbols would you like?"))
numbers = int(input("How many numbers would you like?"))
Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z" ,"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"] 
symbolsTable = ["!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"]
numbersTable = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

password = ""
for i in range(n):
    password.append(r.choice(Alphabet))

for i in range(symbols):
    password.append(r.choice(symbolsTable))

for i in range(numbers):
    password.append(r.choice(numbersTable))

r.shuffle(password)

print(password)
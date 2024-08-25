# # # name = "Angela"
# # # new_list = [char for char in name]
# # # print(new_list)

# # # numbers = [numer*2 for numer in range(1,5)]
# # # print(numbers)
# # names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# # capital_names = [name.upper() for name in names]
# # print   (capital_names) 
# # number = [1, 2, 3, 5, 8, 13, 21, 34, 55]
# # squared_numbers = [number for number in number if number % 2 == 0]
# # print(squared_numbers)  
# # with open("numer1.txt") as file:
# #     names = [int(name.strip()) for name in file]
# #     print(names)
# # with open("number2.txt") as file:
# #     names2 = [int(name.strip()) for name in file]
# #     print(names2)
# # common = [name for name in names if name in names2]
# # print(common)
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# import random
# students_score = {student:random.randint(1,100) for student in names}
# passed_students = {student:score for (student,score) in students_score.items() if score >= 60} 
# print(passed_students)
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word: len(word) for word in sentence.split()}
# print(result) 
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
faraneit = {day :(temp *9/5)+32 for (day,temp) in weather_c.items()} 
print(faraneit)
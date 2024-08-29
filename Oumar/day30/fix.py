# fruits = ['apple', 'banana', 'cherry']
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print('fruit pie')
#     else:
#         print(fruit + ' pie')
# make_pie(4)

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Comments': 4, 'Shares': 3},
    {'Comments': 1, 'Shares': 2},
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        passn
print(total_likes)
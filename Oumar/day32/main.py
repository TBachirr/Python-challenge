##################### Extra Hard Starting Project ######################
# import pandas as pd
# import datetime as dt
# import random
# import smtplib


# 1. Update the birthdays.csv
# data = pd.read_csv("birthdays.csv")
# birthdays = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# name = data["name"].tolist()

# now = dt.datetime.now()
# today = (now.month, now.day)

# if today == birthdays:
#     random_choice = random.choice(name)
#     with open(f"letter_templates/letter_{random_choice}.txt") as letter_file:
#         contents = letter_file.read()
#         contents = contents.replace("[NAME]", random_choice)

#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=passwords)
#         connection.sendmail(
#             from_addr=my_email,
#             to_addrs=other_email,
#             msg=f"Subject:Happy Birthday!\n\n{contents}".encode("utf-8"),
#         )
        
        

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




#To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = "rd144103@gmail.com"
MY_PASSWORD = "ugbh qulb ikez cuwi" 

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

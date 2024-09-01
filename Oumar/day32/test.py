import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()



my_email = "rd144103@gmail.com"
passwords = "ugbh qulb ikez cuwi"  # Assurez-vous que ce mot de passe est correct ou utilisez un mot de passe d'application
other_email = "albap6324@gmail.com"

with open("quote.txt") as quote_file:
    random_quote = random.choice(quote_file.readlines())
    
if weekday == 6:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()  # Sécuriser la connexion
        connection.login(user=my_email, password=passwords)  # Connectez-vous à votre compte
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Hello\n\n{random_quote}".encode("utf-8"),
        )
    print("Email sent successfully")


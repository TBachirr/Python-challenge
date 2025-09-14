import smtplib
MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "test"

class NotificationManager:
    def __init__(self):
        self.my_email = MY_EMAIL
        self.my_password = MY_PASSWORD

    def send_email(self, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.my_email, password=self.my_password)
            connection.sendmail(from_addr=self.my_email, to_addrs=MY_EMAIL, msg=f"Subject:Hello\n\n{message}")  
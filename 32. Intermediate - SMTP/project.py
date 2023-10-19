import smtplib
import datetime as dt
import random

MY_EMAIL = "julianrenechaux@gmail.com"
MY_PASSWORD = "mnlpjvoxockuhrle"

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)

if weekday == 2:
    with open("./quotes.txt") as quote_file:
        #readlines crea una lista de lineas
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        print(quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        #Encriptar el mensaje por seguridad
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs="julianchaux11@yahoo.com.mx", 
            msg=f"Subject:Monday Motivation\n\n{quote}"
            )
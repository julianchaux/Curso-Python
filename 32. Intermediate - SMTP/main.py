import smtplib

#Hotmail: smtp.live.com
#Yahoo: smtp.mail.yahoo.com
my_email = "julianrenechaux@gmail.com"
#App Password - 2-step verification
password = "mnlpjvoxockuhrle"
with smtplib.SMTP("smtp.gmail.com") as connection:
    #Encriptar el mensaje por seguridad
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="julianchaux11@yahoo.com.mx", 
        msg="Subject:Hello from python!\n\nThis is the body."
        )

#Evitamos colocar esta linea si usamos "with"
#connection.close()

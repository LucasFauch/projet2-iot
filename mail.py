import smtplib
import ssl
from email.message import EmailMessage

# Setup port number and servr name

# Standard secure SMTP port
smtp_port = 587
smtp_server = "smtp.gmail.com"

email_from = "projet2iotuqac@gmail.com"
email_to = "ekiam333@gmail.com"

pswd = "qecmbyexhgjvtxoc"

msg = EmailMessage()

body = "Alerte détection anormale de l'utilisation de votre CPU sur votre object connecté."
end_mail = "Envoyé depuis {}".format(email_from)

print(body)

msg.set_content(body)

msg.add_alternative("""<!DOCTYPE html>
<html>
    <body>
        <h2>{}</h2>
        <p>{}</p> 
    </body>
</html>
""".format(body, end_mail), subtype='html')

msg['Subject'] = 'Subject TEST'
msg['From'] = email_from
msg['To'] = email_to

# Create context
simple_email_context = ssl.create_default_context()

try:
    print("Connecting to the server...")
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls(context=simple_email_context)
    server.login(email_from, pswd)
    print("Connection to the server ok")
    print()
    print(f"Sending email to - {email_to}")
    #server.sendmail(email_from, email_to, message)
    server.send_message(msg)
    print(f"Email successfully sent to - {email_to}")

# Print the error if there is one
except Exception as e:
    print(e)

# Close the port
finally:
    server.quit()
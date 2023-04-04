import smtplib
import ssl
from email.message import EmailMessage

class Mail:
    def __init__(self, smtp_port, smtp_server ):
        self.smtp_port = smtp_port
        self.smtp_server = smtp_server
        self.email_from = ""
        self.email_to = ""
        self.password = ""
        self.msg = EmailMessage()

    def setEmailFrom(self, email_from):
        self.email_from = email_from

    def setEmailTo(self, email_to):
        self.email_to = email_to

    def setPassword(self, password):
        self.password = password

    def generateMail(self):
        # Création du mail et des détails nécessaires
        body = "Alerte détection anormale de l'utilisation de votre CPU sur votre object connecté."
        end_mail = "Envoyé depuis {}".format(self.email_from)
        self.msg.set_content(body)

        self.msg.add_alternative("""<!DOCTYPE html>
        <html>
            <body>
                <h2>{}</h2>
                <p>{}</p> 
            </body>
        </html>
        """.format(body, end_mail), subtype='html')

        self.msg['Subject'] = 'Subject TEST'
        self.msg['From'] = self.email_from
        self.msg['To'] = self.email_to
    
    def sendMail(self):
        # Préparation pour l'envoi du mail
        simple_email_context = ssl.create_default_context()
        print(self.smtp_server, self.smtp_port)

        try:
            print("Connexion au serveur...")
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls(context=simple_email_context)
            server.login(self.email_from, self.password)
            print("Connexion au serveur établie")
            #server.sendmail(email_from, email_to, message)
            server.send_message(self.msg)
            print(f"Mail envoyé avec succès à {self.email_to}")

        except Exception as e:
            print(e)

        # Fermeture du port
        finally:
            server.quit()

mail = Mail(587, "smtp.gmail.com")
mail.setEmailFrom("projet2bisiotuqac@gmail.com")
mail.setEmailTo("projet2bisiotuqac@gmail.com")
mail.setPassword("dutcscqvxcrqzaub")
mail.generateMail()
mail.sendMail()

'''
# Mise en place smtp_port et smtp_server
smtp_port = 587
smtp_server = "smtp.gmail.com"

# Informations sur destinataire et expéditeur
email_from = "projet2bisiotuqac@gmail.com"
email_to = "projet2bisiotuqac@gmail.com"
pswd = "dutcscqvxcrqzaub"

# Création du mail et des détails nécessaires
msg = EmailMessage()

body = "Alerte détection anormale de l'utilisation de votre CPU sur votre object connecté."
end_mail = "Envoyé depuis {}".format(email_from)
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

# Préparation pour l'envoi du mail
simple_email_context = ssl.create_default_context()

try:
    print("Connexion au serveur...")
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls(context=simple_email_context)
    server.login(email_from, pswd)
    print("Connexion au serveur établie")
    #server.sendmail(email_from, email_to, message)
    server.send_message(msg)
    print(f"Mail envoyé avec succès à {email_to}")

except Exception as e:
    print(e)

# Fermeture du port
finally:
    server.quit()'''
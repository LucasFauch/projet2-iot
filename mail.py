import smtplib
import ssl
from email.message import EmailMessage

# Mise en place smtp_port et smtp_server
smtp_port = 587
smtp_server = "smtp.gmail.com"

# Informations sur destinataire et expéditeur
email_from = "projet2iotuqac@gmail.com"
email_to = "ekiam333@gmail.com"
pswd = "qecmbyexhgjvtxoc"

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
    server.quit()
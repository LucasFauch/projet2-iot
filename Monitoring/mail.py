import smtplib
import ssl
from email.message import EmailMessage
import datetime
import platform
import logging

class Mail:
    def __init__(self, smtp_port, smtp_server ):
        self.smtp_port = smtp_port
        self.smtp_server = smtp_server
        self.email_from = ""
        self.email_to = ""
        self.password = ""
        self.msg = EmailMessage()
        self.msg['Subject'] = 'Anomalie détectée sur votre object connecté'

    def setSmtpPort(self, smtp_port):
        self.smtp_port = smtp_port

    def setSmtpServer(self, smtp_server):
        self.smtp_server = smtp_server

    def setEmailFrom(self, email_from):
        self.email_from = email_from

    def setEmailTo(self, email_to):
        self.email_to = email_to

    def setPassword(self, password):
        self.password = password

    def setSubjectForMail(self, subject):
        self.msg['Subject'] = subject

    def getProcessusSentance(self, processus):
        return f"{processus[0]} - PID : {processus[1]} avec une utilisation CPU de {processus[2]}%"
    
    def getAllProcessusSentance(self, listProcessus):
        try: 
            processus1 = listProcessus[0]
            processus1 = self.getProcessusSentance(processus1)
        
        except:
            processus1 = "None"

        try: 
            processus2 = listProcessus[1]
            processus2 = self.getProcessusSentance(processus2)
        
        except:
            processus2 = "None"

        try: 
            processus3 = listProcessus[2]
            processus3 = self.getProcessusSentance(processus3)
        
        except:
            processus3 = "None"

        return processus1, processus2, processus3
    
    def generateMail(self, cpu, ram, normalCpu, normalRam, listProcessus=None):
        self.msg['From'] = self.email_from
        self.msg['To'] = self.email_to
    
        body = "Alerte détection anormale de l'utilisation de votre CPU sur votre object connecté."
        endMail = f"Envoyé depuis {self.email_from}"

        heureActuelle = datetime.datetime.now()
        heureActuelle = heureActuelle.strftime("%H:%M:%S")

        date = datetime.datetime.now()
        date = date.strftime("%d-%m-%Y")

        normalCpu = round(normalCpu, 2)
        normalRam = round(normalRam, 2)

        try:
            objectName = platform.node()
        
        except Exception as e:
            objectName = "DefaultName"

        self.msg.set_content(body)

        try:
            nbProcessus = len(listProcessus)
            processus1, processus2, processus3 = self.getAllProcessusSentance(listProcessus)

        except:
            nbProcessus = 0
            processus1, processus2, processus3 = "None", "None", "None"

        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Anomalie sur votre objet connecté</title>
            <style type="text/css">
                body {{
                    background-color: #f4f4f4;
                    font-family: Arial, sans-serif;
                    color: #333333;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    max-width: 600px;
                    margin: auto;
                    padding: 20px;
                    background-color: #ffffff;
                    border-radius: 5px;
                    box-shadow: 0px 0px 10px #cccccc;
                }}
                h1 {{
                    font-size: 24px;
                    color: #333333;
                    margin: 0 0 10px 0;
                }}
                p {{
                    font-size: 16px;
                    line-height: 1.5;
                    margin: 0 0 20px 0;
                }}
                .button {{
                    display: inline-block;
                    padding: 10px 20px;
                    background-color: #00bbff;
                    color: #ffffff;
                    font-size: 16px;
                    text-decoration: none;
                    border-radius: 5px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Anomalie détectée sur votre objet connecté</h1>
                <p>Bonjour,</p>
                <p>Nous avons détecté une anomalie sur votre objet connecté. Veuillez vérifier les informations suivantes :</p>
                <ul>
                    <li>Nom de l'objet : {objectName}</li>
                    <li>Date et heure de l'anomalie : {date} à {heureActuelle}</li>
                    <li>Description de l'anomalie : Utilisation du CPU à {cpu}% au lieu de {normalCpu}% en temps normal, et de la RAM à {ram}% au lieu de {normalRam}% en temps normal</li>
                </ul>
                <p> Liste des {nbProcessus} processus ayant la plus forte consommation de CPU : </p>
                <ul>
                    <li> {processus1} </li>
                    <li> {processus2} </li>
                    <li> {processus3} </li>
                </ul>
                <p>Pour résoudre ce problème, veuillez contacter notre service client en cliquant sur le bouton ci-dessous :</p>
                <p><a href="http://fehmijaafar.net/wiki-iot/index.php?title=Main_Page" class="button">Contacter le service client</a></p>
                <p>Merci,</p>
                <p>L'équipe de support de l'objet connecté</p>
                <p>{endMail}</p>
            </div>
        </body>
        </html>
        """
        
        self.msg.add_alternative(html, subtype='html')
            
    def sendMail(self, logger):
        # Préparation pour l'envoi du mail
        simple_email_context = ssl.create_default_context()
        #logger.info(self.smtp_server, self.smtp_port)

        try:
            logger.info("Connexion au serveur...")
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls(context=simple_email_context)
            server.login(self.email_from, self.password)
            logger.info("Connexion au serveur établie")
            #server.sendmail(email_from, email_to, message)
            server.send_message(self.msg)
            logger.info(f"Mail envoyé avec succès à {self.email_to}")

        except Exception as e:
            logger.error(e)

        # Fermeture du port
        finally:
            server.quit()

'''
mail = Mail(587, "smtp.gmail.com")
mail.setEmailFrom("projet2bisiotuqac@gmail.com")
mail.setEmailTo("projet2bisiotuqac@gmail.com")
mail.setPassword("dutcscqvxcrqzaub")
mail.generateMail(50, 30, 25.547782, 74.47823)
mail.sendMail()'''

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
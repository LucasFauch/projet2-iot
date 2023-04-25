# CPU & RAM Monitoring
import logging
import psutil
import time
import mail as mailUtility

max_allowed_overload = 10  # in percent
time_between_emails = 300  # in seconds
max_allowed_anomalies = 5  # in number of anomalies

logging_name = "monitoring_" + time.strftime("%Y-%m-%d_%H-%M-%S") + ".log"
logging.basicConfig(filename=logging_name, filemode='w', format='%(levelname)s - %(asctime)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def cpu_usage():
    return psutil.cpu_percent(interval=5)


def ram_usage():
    return psutil.virtual_memory()[2]

def getSortedListPID_usageCPU():
    returnList = []

    for p in psutil.process_iter():
        pid = p.pid
        test_list = []
        p.cpu_percent(interval=0.1)
        for i in range(10):
            p_cpu = p.cpu_percent(interval=None)
            time.sleep(0.1)
            test_list.append(p_cpu)
        CPUp = float(sum(test_list))/len(test_list)
                
        CPUpercent = CPUp / psutil.cpu_count()
        returnList.append((pid,CPUpercent))

    returnList.sort(key=lambda a: a[1], reverse=True)
    return returnList


def get_normal_usage():
    cpu = 0
    ram = 0

    # Calculate Normal CPU Usage & Normal RAM Usage during 1 minute
    for i in range(12):
        cpu += cpu_usage()
        ram += ram_usage()
        i += 1

    return cpu / 12, ram / 12


def get_current_usage():
    return cpu_usage(), ram_usage()


def get_anomalies(cpu, ram):
    return cpu > normal_cpu + max_allowed_overload, ram > normal_ram + max_allowed_overload


def send_email(logger, cpu, ram, listProcessus):
    mail = mailUtility.Mail(587, "smtp.gmail.com")
    mail.setEmailFrom("projet2bisbisiotuqac@gmail.com")
    mail.setEmailTo("projet2bisbisiotuqac@gmail.com")
    mail.setPassword("wajrvmghqqhtlqzn")
    mail.generateMail(cpu, ram, normal_cpu, normal_ram, listProcessus)
    mail.sendMail(logger)
    #logger.info("Sending email...")

logger.info("Trying to get normal usage... (1 minute)")
normal_cpu, normal_ram = get_normal_usage()

logger.info("Normal CPU Usage: %.2f %%" % normal_cpu)
logger.info("Normal RAM Usage: %.2f %%" % normal_ram)

anomalies = 0
email_sent_cooldown = 0

while True:
    current_cpu, current_ram = get_current_usage()
    cpu_anomaly, ram_anomaly = get_anomalies(current_cpu, current_ram)

    # print current usage of cpu, with "(Too high!)" if anomaly. logging.warning if anomaly, logging.info else
    logger.warning("Current CPU Usage: %.2f %% (Too High!)" % current_cpu) if cpu_anomaly else logger.info(
        "Current CPU Usage: %.2f %%" % current_cpu)
    logger.warning("Current RAM Usage: %.2f %% (Too High!)" % current_ram) if ram_anomaly else logger.info(
        "Current RAM Usage: %.2f %%" % current_ram)

    anomalies = anomalies + 1 if cpu_anomaly or ram_anomaly else 0

    # if anomalies > 5 and last email was sent more than 5 minutes ago, send email
    if anomalies > max_allowed_anomalies:
        if time.time() - email_sent_cooldown > time_between_emails:
            logger.error("Too many anomalies! Getting the most consuming processes...")
            top3cpu = getSortedListPID_usageCPU()
            for i in range(3):
                logger.info(top3cpu[i])
            processus_mail = []
            for i in range(3):
                pid = top3cpu[i][0]
                cpu = top3cpu[i][1]
                processus_mail.append((psutil.Process(pid).name(), pid, cpu))
            logger.info("Sending email...")
            send_email(logger, current_cpu, current_ram, processus_mail)
            logger.info("Email sent!")
            anomalies = 0
            email_sent_cooldown = time.time()
        else:
            logger.error(
                "Too many anomalies! Email already sent less than %d minutes ago..." % (time_between_emails // 60))

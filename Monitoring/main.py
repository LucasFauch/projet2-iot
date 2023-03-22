# CPU & RAM Monitoring
import psutil
import time
import sys

max_allowed_overload = 10  # in percent
time_between_emails = 300  # in seconds


def cpu_usage():
    return psutil.cpu_percent(interval=5)


def ram_usage():
    return psutil.virtual_memory()[2]


def get_normal_usage():
    cpu = 0
    ram = 0

    # Calculate Normal CPU Usage & Normal RAM Usage during 1 minute
    for i in range(12):
        cpu += cpu_usage()
        ram += ram_usage()
        i += 1
        sys.stderr.write('\rProgress : %.2f %%' % (i * 100 / 12))
        sys.stderr.flush()

    return cpu / 12, ram / 12


def get_current_usage():
    return cpu_usage(), ram_usage()


def get_anomalies(cpu, ram):
    return cpu > normal_cpu + max_allowed_overload, ram > normal_ram + max_allowed_overload


def send_email(cpu, ram):
    email = "TODO send email"

print("Trying to get normal usage... (1 minute)")
normal_cpu, normal_ram = get_normal_usage()

print("\n\nNormal CPU Usage: %.2f %%" % normal_cpu)
print("Normal RAM Usage: %.2f %%\n" % normal_ram)

anomalies = 0
email_sent_cooldown = 0

while True:
    current_cpu, current_ram = get_current_usage()
    cpu_anomaly, ram_anomaly = get_anomalies(current_cpu, current_ram)

    # print current usage of each, with "(Too high!)" if anomaly
    print("\nCurrent CPU Usage: %.2f %%" % current_cpu, "(Too high!)" if cpu_anomaly else "")
    print("Current RAM Usage: %.2f %%" % current_ram, "(Too high!)" if ram_anomaly else "")

    anomalies = anomalies + 1 if cpu_anomaly or ram_anomaly else 0

    # if anomalies > 5 and last email was sent more than 5 minutes ago, send email
    if anomalies > 5:
        if time.time() - email_sent_cooldown > time_between_emails:
            sys.stderr.write("\nToo many anomalies! Sending email...\n")
            send_email(current_cpu, current_ram)
            sys.stderr.write("Email sent!\n")
            anomalies = 0
            email_sent_cooldown = time.time()
        else:
            sys.stderr.write(
                "\nToo many anomalies! Email already sent less than %d ago...\n" % (time_between_emails // 60))

import os


def notifyadmin(emailaddress, host):
    message = "{0} is not responding to ping.".format(host)
    emailData = """echo "{body}" | mailx -s "{subject}" "{to}" """.format(
        body=message, subject=host + " ping error!", to=emailaddress
    )
    os.system(emailData)

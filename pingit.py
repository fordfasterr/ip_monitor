#! /usr/bin/env python3
import pinger
from sendemail import notifyadmin
import sys

if __name__ == "__main__":
    hostname = sys.argv[1]
    email = sys.argv[2]
    print("ping testing:", hostname)

    pingIt = pinger.ping(hostname)
    result = pingIt
    print(result)

    if result == False:
        print(hostname, "Ping error, sending e-mail to sysadmin:", email)
        notifyadmin(email, hostname)
    else:
        print(hostname, "... ping ok!")

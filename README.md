# ip_monitor
Esteban Arniella, Sept, 2018.

This program will test an ip or hostname via ping, and e-mail the admin if it fails.

It is suitable for use via cron job.

It only works on linux variants.

It takes 2 arguments, the ip or hostname, and the e-mail adddress.

It also relies on the os mailx utility from mailutils package.
# usage: ./pingit \<ip or hostname> \<e-mail address>

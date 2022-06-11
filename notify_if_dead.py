"""
Put your own token and stuff in here. This should run via cron/systemd every minute, set the "max_delay" value to the number of minutes it can be dead for before yelling about it. 
"""

from twilio.rest import Client
import os
from datetime import datetime, timedelta

auth_token  = "HAHAHAHAHAHAHAHAHANOPE"
account_sid = "NOPENOPENOPENOPENOPENOPE"
twilio_phone_num = +12223334455
notify_phone_num = +11234567890

client = Client(account_sid, auth_token)
file_mod_time = datetime.fromtimestamp(os.stat('/home/epss_check/scripts/last_check').st_mtime)
now = datetime.today()
max_delay = timedelta(minutes=15)

if now - file_mod_time > max_delay:
    message = client.messages.create(
        to=f"{notify_phone_num}",
        from_=f"{twilio_phone_num}",
        body=f"EPSS Bot here,\n My last contact with Campus was {int((now-file_mod_time).seconds/60)} minutes ago\n You should check its not a power outage!"
    )

else:
    print (f"OK. Command completed successfully {(now-file_mod_time).seconds/60} minutes ago.")

print(file_mod_time)
print(datetime.now())

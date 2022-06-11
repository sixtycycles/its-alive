"""
leave this on the server that is off site, serving as "check in host"
"""
from datetime import datetime

with open ("/home/epss_check/scripts/last_check" , 'r') as check:
    num = check.readlines()
    check.close()

with open ("/home/epss_check/scripts/last_check", "w+") as checkin:
    checkin.writelines(f"still here! {datetime.now()} \n")
    print("checked in")
    checkin.close()

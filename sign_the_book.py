"""
leave this on the server that is off site, serving as "check in"  this opens a file
"""

from datetime import datetime
# was going to do a check here, but didn't. lose this: 
# with open ("/home/epss_check/scripts/last_check" , 'r') as check:
#     num = check.readlines()
#     check.close()

with open ("/home/epss_check/scripts/last_check", "w") as checkin:
    checkin.writelines(f"still here! {datetime.now()} \n")
    print("checked in")
    checkin.close()

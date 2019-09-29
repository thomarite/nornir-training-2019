from nornir import InitNornir
from nornir.core.task import Result
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from pprint import pprint

import re

# Easier to store these as constants
HOUR_SECONDS = 3600
DAY_SECONDS = 24 * HOUR_SECONDS
WEEK_SECONDS = 7 * DAY_SECONDS
YEAR_SECONDS = 365 * DAY_SECONDS


def parse_uptime(uptime_str):
    """Based on method in the NAPALM library"""
    # import ipdb; ipdb.set_trace()

    if "uptime is" in uptime_str:
        # IOS/NX-OS
        uptime_str = uptime_str.split("uptime is")[1]
    elif "Uptime:" in uptime_str:
        # Arista
        uptime_str = uptime_str.split("Uptime: ")[1]
    else:
        # Juniper - different text form
        # System booted: 2018-10-03 20:51:06 PDT (44w1d 01:59 ago)
        # pretend it just rebooted
        return 90

    # Initialize to zero
    (years, weeks, days, hours, minutes) = (0, 0, 0, 0, 0)

    uptime_str = uptime_str.strip()

    # Replace 'and' in Arista uptime with a comma so values get split appropriately
    uptime_str = uptime_str.replace("and", ",")

    time_list = uptime_str.split(",")
    #print(time_list)
    for element in time_list:
        if re.search("year", element):
            years = int(element.split()[0])
        elif re.search("week", element):
            weeks = int(element.split()[0])
        elif re.search("day", element):
            days = int(element.split()[0])
        elif re.search("hour", element):
            hours = int(element.split()[0])
        elif re.search("minute", element):
            minutes = int(element.split()[0])

    uptime_sec = (
        (years * YEAR_SECONDS)
        + (weeks * WEEK_SECONDS)
        + (days * DAY_SECONDS)
        + (hours * 3600)
        + (minutes * 60)
    )
    return uptime_sec

def my_uptime(task):
   #keep in mind that you are in a thread when executing this task
   #import ipdb; ipdb.set_trace()
   #print(task.host.groups[0])
   cmd = ""
   if (task.host.groups[0] == "ios") or (task.host.groups[0] == "nxos"):
      cmd = "show version | inc uptime"
   elif task.host.groups[0] == "junos":
      cmd = "show system uptime | match System"
   elif task.host.groups[0] == "eos":
      cmd = "show version | inc Uptime"
   else:
      print("device group UNKNOW! - exit program")
      exit()
 
   results = task.run(task=networking.netmiko_send_command, command_string=cmd)

   ## the exercise states we need to modify junos uptime to 90 sec
   uptime_sec = 0 
   if task.host.groups[0] == "junos":
      uptime_sec = 90
   else:
      uptime_sec = parse_uptime(results[0].result)

   ## if device uptime is less than 1 day, give message
   message = ""
   if uptime_sec < DAY_SECONDS:
      message = " --- device has rebooted in the last 24 hours!!! - PLEASE VERIFY" 
   print(f"{task.host.hostname} uptime = {uptime_sec} sec {message}")
   print()


def main():
   #nr = InitNornir(config_file="config.yaml")
   nr = InitNornir(config_file="config.yaml", logging={"enabled": False})
   print()
   nr.run(task=my_uptime)
   #print_result(results)

if __name__ == "__main__":
   main()

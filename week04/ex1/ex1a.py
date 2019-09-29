from nornir import InitNornir
from nornir.core.task import Result
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from pprint import pprint

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
   print(f"{task.host.hostname} uptime = {results[0].result}")
   print()


def main():
   #nr = InitNornir(config_file="config.yaml")
   nr = InitNornir(config_file="config.yaml", logging={"enabled": False})
   print()
   nr.run(task=my_uptime)
   #print_result(results)

if __name__ == "__main__":
   main()

from nornir import InitNornir
from nornir.core.filter import F
from nornir.core.task import Result
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from pprint import pprint

def add_vlan(task, vlan_id, vlan_name):
   #keep in mind that you are in a thread when executing this task
   #import ipdb; ipdb.set_trace()
   #print(task.host.groups[0])
   cmd = ""
   if (task.host.groups[0] == "nxos"):
      cmd = "show version | inc uptime"
   elif task.host.groups[0] == "eos":
      cmd = "show version | inc Uptime"
   else:
      print("device group UNKNOW! - exit program")
      exit()

   # diret inline configs
   commands = ["vlan " + str(vlan_id), "name " + vlan_name ] 
   results = task.run(task=networking.netmiko_send_config, config_commands=commands)

def main():
   nr = InitNornir(config_file="config.yaml")
   nr = nr.filter(F(groups__contains="nxos") | F(groups__contains="eos"))
   nr.run(task=add_vlan, vlan_id = 100, vlan_name = "tmorales-ex3a")
   #print_result(results)

if __name__ == "__main__":
   main()

from nornir import InitNornir
from nornir.core.filter import F
from nornir.core.task import Result
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from pprint import pprint

import re

def add_vlan(task, vlan_id, vlan_name):
   #keep in mind that you are in a thread when executing this task
   #import ipdb; ipdb.set_trace()

   # build command to check if the vlan exist with the required name
   cmd = ""
   if (task.host.groups[0] == "nxos"):
      cmd = "show vlan | i " + str(vlan_id) + " | i active"
   elif task.host.groups[0] == "eos":
      cmd = "show vlan | i " + str(vlan_id)
   else:
      print("device group UNKNOW! - exit program")
      exit()
   print("cmd = " + cmd)

   # send command and take result
   results = task.run(task=networking.netmiko_send_command, command_string=cmd)
   vlan_query = results[0].result
   print(vlan_query)

   '''
   Check if the vlan number and vlan name exist in the output of the command sent earlier

   nxos1# show vlan | i 100 | i active
   100  tmorales-ex3a                    active    

   arista1#show vlan | i 100
   100   tmorales-ex3a                    active   

   If one clause if false, we add the vlan/name
   '''
   #import ipdb; ipdb.set_trace()
   if re.search(str(vlan_id), vlan_query) and re.search(vlan_name, vlan_query):
      print("vlan already exists")
      return Result(host=task.host, changed = False, failed = False, result = "vlan already exists")
   else:
      commands = ["vlan " + str(vlan_id), "name " + vlan_name ] 
      results = task.run(task=networking.netmiko_send_config, config_commands=commands)
      print("vlan created")
      return Result(host=task.host, changed = True, failed = False, result = "vlan created")

def main():
   nr = InitNornir(config_file="config.yaml")
   nr = nr.filter(F(groups__contains="nxos") | F(groups__contains="eos"))
   results = nr.run(task=add_vlan, vlan_id = 100, vlan_name = "tmorales-ex3a", num_workers=10)
   print_result(results)

if __name__ == "__main__":
   main()

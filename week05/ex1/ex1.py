from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_config
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result

def add_snmp_id(task):
   commands = []
   if "ios" in task.host.groups:
      commands=[f"snmp-server chassis-id {task.host['snmp_id']}"]
   elif "eos" in task.host.groups:
      commands=[f"snmp chassis-id {task.host['snmp_id']}-{task.host.hostname}"]
   else:
     exit(1) 
   results = task.run(task=netmiko_send_config, config_commands=commands)
   #print(results[0].result)

if __name__ == "__main__":
   nr = InitNornir(config_file="config.yaml")
   nr = nr.filter(F(groups__contains="ios") | F(groups__contains="eos"))
   results = nr.run(task=add_snmp_id)
   #import ipdb; ipdb.set_trace()
   print_result(results)    


from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

def send_command(task, cmd=""):
   results = task.run(task=netmiko_send_command, command_string=cmd)
   if "syntax error" in results[0].result:
      #print("ERROR DETECTED!")
      raise ValueError("Invalid Junos command")

if __name__ == "__main__":
   nr = InitNornir(config_file="config.yaml")
   nr = nr.filter(name="srx2")
   results = nr.run(task=send_command, cmd="show ip interface brief")
   #import ipdb; ipdb.set_trace()
   print_result(results)    


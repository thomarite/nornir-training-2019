from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.core.filter import F

def main():
   nr = InitNornir(config_file="config.yaml")
   eos = nr.filter(F(groups__contains="eos"))
   results = eos.run(task=netmiko_send_command, command_string="show interface status", use_textfsm=True)
   #import ipdb; ipdb.set_trace()
   for device in results.keys():
      print()
      print("results show int status in", device, "is", results[device][0].result)

if __name__ == "__main__":
   main()

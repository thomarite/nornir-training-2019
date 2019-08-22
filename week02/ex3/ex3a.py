from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
import ipdb
import re

def main():
   nr = InitNornir(config_file="config.yaml")
   ios_filt = F(groups__contains="ios")
   eos_filt = F(groups__contains="eos")
   nr = nr.filter(ios_filt | eos_filt)
   results = nr.run(task=netmiko_send_command, command_string="show ip arp")
   #ipdb.set_trace()
   for host, multi_result in results.items():
      # multi_result is a list and in this example only has one element
      output = multi_result[0].result
      desired_data = ""
      for line in output.splitlines():
         if "10.220.88.1" in line:
            desired_data = re.sub(r"\s+", " ", line)
            print(f"Host: {host}, Gateway: {desired_data}")
            break

if __name__ == "__main__":
   main()


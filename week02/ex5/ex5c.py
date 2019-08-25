from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result
import os

def main():
   nr = InitNornir(config_file="config.yaml")
   ios_filt = F(groups__contains="ios")
   nr = nr.filter(ios_filt)
   nr.inventory.hosts["cisco3"].password = 'bogus'
   results = nr.run(task=netmiko_send_command, command_string="show ip int brief")
   print("results.failed_hosts:",results.failed_hosts)
   print("nr.data.failed_hosts:",nr.data.failed_hosts)
   # recover cisco3 password and repeat process
   nr.inventory.hosts["cisco3"].password = os.environ["NORNIR_PASSWORD"]
   # The issue here is that Nornir keeps track of existing connections and once the connection fails it does not retry the connection again.
   try:
      # Remove "cisco3" from the Nornir connection table
      nr.inventory.hosts["cisco3"].close_connections()
   except ValueError:
      pass
   results = nr.run(task=netmiko_send_command, on_failed=True, on_good=False, command_string="show ip int brief")
   print_result(results)
   print("results.failed_hosts:",results.failed_hosts)
   print("nr.data.failed_hosts:",nr.data.failed_hosts)

if __name__ == "__main__":
   main()


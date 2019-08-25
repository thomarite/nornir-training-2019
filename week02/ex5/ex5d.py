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
   print("First pass")
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
   
   print()
   print("Second pass after updaing cisco3 password")
   print("Task failed hosts: results.failed_hosts:",results.failed_hosts)
   print("Global failed hosts: nr.data.failed_hosts:",nr.data.failed_hosts)
   #import ipdb; ipdb.set_trace()
   
   # recover failed hosts
   nr.data.recover_host('cisco3')
   #for failed_host in nr.data.failed_hosts:
   #   nr.data.recover_host(failed_host)
   # check again the status of failed hosts, as now, everything should be recovered
   print()
   print("Check status after recovering failed hosts")
   print("Task failed hosts: results.failed_hosts:",results.failed_hosts)
   print("Global failed hosts: nr.data.failed_hosts:",nr.data.failed_hosts)


if __name__ == "__main__":
   main()


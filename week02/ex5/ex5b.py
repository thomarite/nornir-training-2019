from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command

def main():
   nr = InitNornir(config_file="config.yaml")
   ios_filt = F(groups__contains="ios")
   nr = nr.filter(ios_filt)
   nr.inventory.hosts["cisco3"].password = 'bogus'
   results = nr.run(task=netmiko_send_command, command_string="show ip int brief")
   print("results.failed_hosts:",results.failed_hosts)
   print("nr.data.failed_hosts:",nr.data.failed_hosts)

if __name__ == "__main__":
   main()


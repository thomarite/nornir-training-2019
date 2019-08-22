from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result

def main():
   nr = InitNornir(config_file="config.yaml")
   ios_filt = F(groups__contains="ios")
   nr = nr.filter(ios_filt)
   results = nr.run(task=netmiko_send_command, command_string="show ip int brief")
   print_result(results)

if __name__ == "__main__":
   main()


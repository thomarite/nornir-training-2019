from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command

def main():
   nr = InitNornir(config_file="config.yaml")
   filt = F(groups__contains="ios")
   nr = nr.filter(filt)
   results = nr.run(task=netmiko_send_command, command_string="show run | inc hostname")

   print("type :",type(results))
   print("keys:",results.keys())
   print("items:",results.items())
   print("values:",results.values)

if __name__ == "__main__":
   main()


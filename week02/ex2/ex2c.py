from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
import ipdb


def main():
   nr = InitNornir(config_file="config.yaml")
   filt = F(groups__contains="ios")
   nr = nr.filter(filt)
   results = nr.run(task=netmiko_send_command, command_string="show run | inc hostname")
   host_results = results['cisco3']

   #ipdb.set_trace()

   print("[0] :",host_results[0])
   print("dir outout:",dir(host_results))

   #  I dont undestand this solution
   print()
   print(type(host_results))
   print(repr(host_results[0]))
   print(host_results.__iter__)
   print()


if __name__ == "__main__":
   main()


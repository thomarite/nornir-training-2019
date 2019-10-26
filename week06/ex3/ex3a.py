from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import text
from nornir.core.filter import F
from getpass import getpass

#PASSWORD = getpass()
PASSWORD = "88newclass"

def main():                                                                                 
  nr = InitNornir(config_file="config.yaml")
  nr = nr.filter(name="arista1")
  import ipdb; ipdb.set_trace()
  nr.inventory.password = PASSWORD
  agg_result = nr.run(task=networking.netmiko_send_command, command_string="show run | i hostname", enable=True)


if __name__ == "__main__":
  main()

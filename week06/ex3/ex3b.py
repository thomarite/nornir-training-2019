from nornir import InitNornir
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import text
from nornir.core.filter import F
from getpass import getpass

import logging

logger = logging.getLogger("nornir")

PASSWORD = getpass()
#PASSWORD = "88newclass"

def main():                                                                                 
  nr = InitNornir(config_file="config.yaml")
  nr = nr.filter(name="arista1")
  for host, host_obj in nr.inventory.hosts.items():
     host_obj.password = PASSWORD
  #import ipdb; ipdb.set_trace()
  agg_result = nr.run(task=networking.netmiko_send_command, command_string="show run | i hostname")
  print_result(agg_result)
  logger.critical("CRITICAL")
  logger.error("ERROR")
  logger.debug("DEBUG")


if __name__ == "__main__":
  main()

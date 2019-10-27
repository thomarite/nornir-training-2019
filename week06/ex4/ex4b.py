from nornir import InitNornir
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import text
from nornir.core.filter import F
import os

PASSWORD = os.environ.get("NORNIR_PASSWORD", "missing") # If the password is not defined, use "bogus"


def my_task(task):
  # dynamically set the session_log to be unique per host
  filename = f"{task.host}-output.txt"
  group_object = task.host.groups.refs[0] # <--- "refs" is something special!!!!!!!!!!!!!!!
  group_object.connection_options["netmiko"].extras["session_log"] = filename
  task.run(task=networking.netmiko_send_command, command_string="show run | i hostname")


def main():                                                                                 
  nr = InitNornir(config_file="config.yaml")
  nr = nr.filter(F(groups__contains="nxos"))
  for host, host_obj in nr.inventory.hosts.items():
     host_obj.password = PASSWORD
     #import ipdb; ipdb.set_trace()
  agg_result = nr.run(task=my_task)
  print_result(agg_result)

if __name__ == "__main__":
  main()

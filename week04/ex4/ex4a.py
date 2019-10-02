from nornir import InitNornir
from nornir.core.filter import F
from nornir.core.task import Result
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from pprint import pprint

import re

def add_vlan(task, vlan_id, vlan_name):
   #keep in mind that you are in a thread when executing this task
   #import ipdb; ipdb.set_trace()

   vlan_cmd = "vlan " + str(vlan_id) + "\n" + "name " + vlan_name

   # using string + dry_run=True (no making changes -> noop)
   results = task.run(task=networking.napalm_configure, configuration=vlan_cmd, dry_run=False)

def main():
   nr = InitNornir(config_file="config.yaml")
   nr = nr.filter(F(groups__contains="nxos") | F(groups__contains="eos"))
   results = nr.run(task=add_vlan, vlan_id = 101, vlan_name = "tmorales-ex4a", num_workers=1)
   print_result(results)

if __name__ == "__main__":
   main()

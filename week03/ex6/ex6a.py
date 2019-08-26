from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get
from nornir.core.filter import F
from pprint import pprint
from nornir.plugins.functions.text import print_result

def main():
   nr = InitNornir(config_file="config.yaml")
   nxos = nr.filter(F(groups__contains="nxos"))
   results = nxos.run(task=napalm_get, getters=["config"])
   #import ipdb; ipdb.set_trace()
   print_result(results)

if __name__ == "__main__":
   main()

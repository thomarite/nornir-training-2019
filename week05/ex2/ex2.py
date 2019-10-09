from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result

def get_eos_config(task):
   result = task.run(task=napalm_get, getters=["config"], retrieve="running")
   #import ipdb; ipdb.set_trace()

if __name__ == "__main__":
   nr = InitNornir(config_file="config.yaml")
   nr = nr.filter(F(groups__contains="eos"))
   results = nr.run(task=get_eos_config)
   print_result(results)    


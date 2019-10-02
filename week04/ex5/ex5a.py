from nornir import InitNornir
from nornir.core.filter import F
from nornir.core.task import Result
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from pprint import pprint

def main():
   nr = InitNornir(config_file="config.yaml")
   nr = nr.filter(name='arista4')
   result = nr.run(task=networking.napalm_get, getters=["config"], retrieve="running")
   arista4_running = result["arista4"].result["config"]["running"]
   pprint(arista4_running)

if __name__ == "__main__":
   main()

from nornir import InitNornir
from nornir.core.filter import F
from nornir.core.task import Result
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result
from pprint import pprint

arista_loopback = """interface loopback123
 description Done by tmorales-ex5b"""

def main():
   nr = InitNornir(config_file="config.yaml")
   nr = nr.filter(name='arista4')
   result = nr.run(task=networking.napalm_configure, configuration=arista_loopback)
   print_result(result)

if __name__ == "__main__":
   main()

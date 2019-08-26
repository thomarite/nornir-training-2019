from nornir import InitNornir
from nornir.core.filter import F

def main():
   nr = InitNornir(config_file="config.yaml")
   print()
   print("hosts:", nr.inventory.hosts)
   #import ipdb; ipdb.set_trace()

if __name__ == "__main__":
   main()

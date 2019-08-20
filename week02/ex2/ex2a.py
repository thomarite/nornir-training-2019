from nornir import InitNornir
from nornir.core.filter import F

def main():
   nr = InitNornir(config_file="config.yaml")
   filt = F(groups__contains="ios")
   nr = nr.filter(filt)
   print(nr.inventory.hosts)

if __name__ == "__main__":
   main()


from nornir import InitNornir
from nornir.core.filter import F

def main():
   nr = InitNornir()
   nrf = nr.filter(F(groups__contains="sfo"))
   print()
   print("hosts via filter sfo:", nrf.inventory.hosts)
   #import ipdb; ipdb.set_trace()

if __name__ == "__main__":
   main()

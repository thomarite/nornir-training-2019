from nornir import InitNornir
from nornir.core.filter import F

def main():
   nr = InitNornir()
   nrf = nr.filter(F(role="AGG"))
   #nrf = nr.filter(F(role__contains="AGG"))
   print()
   print("hosts via filter role AGG:", nrf.inventory.hosts)
   #import ipdb; ipdb.set_trace()

if __name__ == "__main__":
   main()

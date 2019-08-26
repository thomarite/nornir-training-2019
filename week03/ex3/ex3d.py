from nornir import InitNornir
from nornir.core.filter import F

def main():
   nr = InitNornir()
   nrf = nr.filter(F(role="WAN") & ~F(site_details__wifi_password__contains="racecar"))
   print()
   print("hosts via filter WAN and not racecar:", nrf.inventory.hosts)
   #import ipdb; ipdb.set_trace()

if __name__ == "__main__":
   main()

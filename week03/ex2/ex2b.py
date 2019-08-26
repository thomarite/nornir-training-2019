from nornir import InitNornir

def main():
   nr = InitNornir()
   nrf1 = nr.filter(role="WAN")
   print()
   print("hosts via filter role:", nrf1.inventory.hosts)
   #import ipdb; ipdb.set_trace()
   nrf2 = nrf1.filter(port=22)
   print()
   print("hosts via filter role and port:", nrf2.inventory.hosts)

if __name__ == "__main__":
   main()

from nornir import InitNornir

def main():
   nr = InitNornir()
   nrf = nr.filter(name='arista1')
   print()
   print("hosts via filter:", nrf.inventory.hosts)
   #import ipdb; ipdb.set_trace()

if __name__ == "__main__":
   main()

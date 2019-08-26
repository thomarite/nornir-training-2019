from nornir import InitNornir

def main():
   nr = InitNornir()
   print()
   #import ipdb; ipdb.set_trace()
   for k,v in nr.inventory.hosts.items():
      print("host:", k, " timezone:", v['timezone'])

if __name__ == "__main__":
   main()

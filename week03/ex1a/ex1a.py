from nornir import InitNornir

def main():
   nr = InitNornir()
   print()
   print("arista3 data at host level:", nr.inventory.hosts['arista3'].data)
   print()
   print("arista3 items method:", dict(nr.inventory.hosts['arista3'].items()))


if __name__ == "__main__":
   main()

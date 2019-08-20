from nornir import InitNornir

def main():
   nr = InitNornir()
   print("Num of workers is", nr.config.core.num_workers)

if __name__ == "__main__":
   main()


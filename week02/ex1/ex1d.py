from nornir import InitNornir

def main():
   nr = InitNornir(config_file="config.yaml", core={"num_workers": 15})
   print("Num of workers is", nr.config.core.num_workers)

if __name__ == "__main__":
   main()


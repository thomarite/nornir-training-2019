from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import napalm_get
import ipdb

def main():
   nr = InitNornir(config_file="config.yaml")
   ios_filt = F(groups__contains="ios")
   eos_filt = F(groups__contains="eos")
   nr = nr.filter(ios_filt | eos_filt)
   results = nr.run(task=napalm_get,getters=["arp_table"])
   #ipdb.set_trace()
   for host, multi_result in results.items():
      # multi_result is a list and in this example only has one element
      arp_table = multi_result[0].result['arp_table']
      for arp_entry in arp_table:
         if "10.220.88.1" in arp_entry['ip']:
            print(f"Host: {host}, Gateway: {arp_entry}")
            break

if __name__ == "__main__":
   main()


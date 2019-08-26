from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.core.filter import F
from pprint import pprint

def main():
   nr = InitNornir(config_file="config.yaml")
   eos = nr.filter(F(groups__contains="eos"))
   results = eos.run(task=netmiko_send_command, command_string="show interface status", use_textfsm=True)
   #import ipdb; ipdb.set_trace()
   final_dict = {}
   for device in results.keys():
      final_dict[device] = {}
      for line in results[device][0].result:
         final_dict[device][line['port']]={}
         final_dict[device][line['port']]['status']=line['status']
         final_dict[device][line['port']]['vlan']=line['vlan']
   print()
   pprint(final_dict)

if __name__ == "__main__":
   main()

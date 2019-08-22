from nornir import InitNornir
from nornir.core.filter import F
from nornir.plugins.tasks.networking import netmiko_send_command
import ipdb


def main():
   nr = InitNornir(config_file="config.yaml")
   filt = F(groups__contains="ios")
   nr = nr.filter(filt)
   results = nr.run(task=netmiko_send_command, command_string="show run | inc hostname")
   host_results = results['cisco3']

   #ipdb.set_trace()

   print("host_results[0] :",host_results[0])
   print("dir output:",dir(host_results))

   task_result = host_results[0]
   print("task_result type = ",type(task_result))
   print("host = ",task_result.host)
   print("task name = ",task_result.name)
   print("result = ",task_result.result)
   print("failed = ",task_result.failed)

if __name__ == "__main__":
   main()


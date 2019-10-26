from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import text
from nornir.core.filter import F

def my_task(task):
   #import ipdb; ipdb.set_trace()
   result = task.run(task=text.template_file, template="nxos-loopback.j2", path=".", **task.host)
   print(result[0].result) 

def main():
  nr = InitNornir(config_file="config.yaml", logging={"enabled": False})
  nr = nr.filter(groups=["nxos"])
  result = nr.run(task=my_task, num_workers=1)
  print_result(result)

if __name__ == "__main__":
  main()


from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import text
from nornir.core.filter import F
from nornir.core.exceptions import NornirSubTaskError

def my_task(task):
  try:
    result = task.run(task=text.template_file, template="nxos-loopback.j2", path=".", **task.host)
  except NornirSubTaskError:
    return "Host missing data for generating loopback config"

def main():
  nr = InitNornir(config_file="config.yaml", logging={"enabled": False})
  nr = nr.filter(groups=["nxos"])
  result = nr.run(task=my_task, num_workers=1)
  #import ipdb; ipdb.set_trace()
  print_result(result)

if __name__ == "__main__":
  main()


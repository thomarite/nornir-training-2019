from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import text
from nornir.core.filter import F
from nornir.core.exceptions import NornirSubTaskError
from nornir.core.task import Result

def my_task(task):
   #import ipdb; ipdb.set_trace()
   try:
     result = task.run(task=text.template_file, template="nxos-loopback.j2", path=".", **task.host)
   except NornirSubTaskError:
     task.results.pop()
     msg = "Encountered Jinja2 error"
     return Result(
       changed=False,
       diff=None,
       result=msg,
       host=task.host,
       failed=False,
       exception=None,
       ) 

def main():
  nr = InitNornir(config_file="config.yaml", logging={"enabled": False})
  nr = nr.filter(groups=["nxos"])
  result = nr.run(task=my_task, num_workers=1)
  import ipdb; ipdb.set_trace()
  print_result(result)

if __name__ == "__main__":
  main()


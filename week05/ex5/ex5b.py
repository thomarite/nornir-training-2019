from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import text
from nornir.plugins.tasks import files
from nornir.plugins.tasks import data
from nornir.core.filter import F

def write_configs(task):
  config_path = f"./rendered/"
  if task.host['interfaces_config']:
    filename = f"{config_path}{task.host.name}_interfaces"
    content = task.host['interfaces_config']
    task.run(task=files.write_file, filename=filename, content=content)
  if task.host['bgp_config']:
    filename = f"{config_path}{task.host.name}_bgp"
    content = task.host['bgp_config']
    task.run(task=files.write_file, filename=filename, content=content)

def nxos_interfaces(task):
  template_path = f"./{task.host.platform}/"
  template = "interface.j2"
  result = task.run(task=text.template_file, template=template, path=template_path, **task.host)
  task.host['interfaces_config'] = result[0].result

def nxos_bgp(task):
  template_path = f"./{task.host.platform}/"
  template = "bgp.j2"
  result = task.run(task=text.template_file, template=template, path=template_path, **task.host)
  task.host['bgp_config'] = result[0].result
  
def main():
  nr = InitNornir(config_file="config.yaml", logging={"enabled": False})
  nr = nr.filter(F(groups__contains="nxos"))
  nr.run(task=nxos_interfaces)
  nr.run(task=nxos_bgp)
  write = nr.run(task=write_configs)
  print_result(write)
  
if __name__ == "__main__":
   main()


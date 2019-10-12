from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import text
from nornir.plugins.tasks import files
from nornir.plugins.tasks import data


def render_configs(task):
  template_path = f"templates/{task.host.platform}/"
  template = "interfaces.j2"
  result = task.run(tas=text.template_file, template=template, path=template_path, **task.host)
  render_config = result[0].result
  task.host['render_config'] = render_config
  
def write_configs(task):
  config_path = f"configs/{task.host.platform}/"
  filename = f"{config_path}{task.host.name}_interfaces"
  content = task.host['render_config']
  result = task.run(task=files.write_file, filename=filename, content=content)


def nxos_interface(task):
  # Load the YAML-ACL entries
  in_yaml = task.run(task=data.load_yaml, file=f"acl.yaml")
  in_yaml = in_yaml[0].result
  #task.host['acl'] = in_yaml
  #print(task.host['acl'])

  template_path = f"templates/{task.host.platform}/"
  template = "acl.j2"
  #result = task.run(task=text.template_file, template=template, path=template_path, **task.host)
  result = task.run(task=text.template_file, template=template, path=template_path, acl=in_yaml)
  task.host['acl'] = result[0].result
  #print(task.host['acl'])
  
def main():
  nr = InitNornir(config_file="config.yaml", logging={"enabled": False})
  nr = nr.filter(name="nxos1" | name="nxos2")
  render = nr.run(task=junos_acl)
  print_result(render)
  
if __name__ == "__main__":
   main()


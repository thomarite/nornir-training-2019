from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import text
from nornir.plugins.tasks import files
from nornir.plugins.tasks import data

def junos_acl(task):
  # Load the YAML-ACL entries
  in_yaml = task.run(task=data.load_yaml, file=f"acl.yaml")
  in_yaml = in_yaml[0].result
  #task.host['acl'] = in_yaml
  #print(task.host['acl'])

  template_path = f"templates/{task.host.platform}/"
  template = "acl.j2"
  #result = task.run(task=text.template_file, template=template, path=template_path, **task.host)
  result = task.run(task=text.template_file, template=template, path=template_path, acl=in_yaml)
  render_config = result[0].result
  task.host['render_config'] = render_config
  print(render_config)
  
def main():
  nr = InitNornir(config_file="config.yaml", logging={"enabled": False})
  nr = nr.filter(name="srx2")
  render = nr.run(task=junos_acl)
  print_result(render)
  
if __name__ == "__main__":
   main()


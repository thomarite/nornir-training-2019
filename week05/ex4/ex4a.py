from nornir import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks import text
from nornir.plugins.tasks import files
from nornir.plugins.tasks import data

TEMPLATE_ACL = \
"""{% for acl_name, acl_entries in acl.items() %}
{% for data in acl_entries %}
set firewall family inet filter {{ acl_name }} term {{ data['term_name'] }} from protocol {{ data['protocol'] }}
set firewall family inet filter {{ acl_name }} term {{ data['term_name'] }} from destination-port {{ data['destination_port'] }}
set firewall family inet filter {{ acl_name }} term {{ data['term_name'] }} from destination-address {{ data['destination_address'] }}
set firewall family inet filter {{ acl_name }} term {{ data['term_name'] }} then {{ data['state'] }}
{% endfor %}
{% endfor %}"""

def junos_acl(task):
  # Load the YAML-ACL entries
  in_yaml = task.run(task=data.load_yaml, file=f"acl.yaml")
  in_yaml = in_yaml[0].result
  task.host['acl'] = in_yaml
  #print(task.host['acl'])

  result = task.run(task=text.template_string, template=TEMPLATE_ACL, acl=in_yaml)
  result[0].result
  
def main():
  nr = InitNornir(config_file="config.yaml", logging={"enabled": False})
  nr = nr.filter(name="srx2")
  render = nr.run(task=junos_acl)
  print_result(render)
  
if __name__ == "__main__":
   main()


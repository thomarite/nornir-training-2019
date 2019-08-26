from nornir import InitNornir
from nornir.plugins.tasks.networking import napalm_get
from nornir.core.filter import F
from pprint import pprint
from nornir.plugins.functions.text import print_result

def main():
   nr = InitNornir(config_file="config.yaml")
   nxos = nr.filter(F(groups__contains="nxos"))
   results = nxos.run(task=napalm_get, getters=["config", "facts"], getters_options={"config": {"retrieve": "all"}})
   output = {}
   for device, mresults in results.items():
      output[device] = {}
      dev_result = mresults[0]  # We are running only one task so we take the first entry
      startup = dev_result.result['config']['startup'].split("\n")[5:]
      running = dev_result.result['config']['running'].split("\n")[5:]
      import ipdb; ipdb.set_trace()
      output[device]['start_running_match'] = (startup == running)
      output[device]['model'] = dev_result.result['facts']['model']
      output[device]['uptime'] = dev_result.result['facts']['uptime']
      output[device]['vendor'] = dev_result.result['facts']['vendor']

   pprint(output)

if __name__ == "__main__":
   main()

from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_file_transfer
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.core.filter import F
from nornir.plugins.functions.text import print_result


def file_copy(task):
    #import ipdb; ipdb.set_trace()
    # Obtain the group_name
    group_name = task.host.platform
    # Set the filename from the group data
    base_file = "arista1_test.txt"
    dest_file = f"{group_name}/{task.host.hostname}-saved.txt"
    #print(source_file)

    # Transfer the file
    results = task.run(
        netmiko_file_transfer,
        source_file=base_file,
        dest_file=dest_file,
        direction="get",
    )
    if results[0].result is True:
        return f"SCP get completed: {dest_file}"
    else:
        return f"Failure...SCP get failed!!!"


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml")
    eos = nr.filter(F(groups__contains="eos"))
    results = eos.run(task=file_copy, num_workers=10)
    print_result(results)


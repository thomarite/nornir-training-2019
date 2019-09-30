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
    base_file = task.host["file_name"]
    source_file = f"{group_name}/{base_file}"
    #print(source_file)

    # Transfer the file
    results = task.run(
        netmiko_file_transfer,
        source_file=source_file,
        dest_file=base_file,
        overwrite_file=True,
        direction="put",
    )
    # Verify transfer
    cmd = "more flash:/arista1_test.txt"
    results = task.run(task=netmiko_send_command, command_string=cmd)
    print(f"{task.host.hostname} content file\n{results[0].result}")
    print("-" * 40)
    print()


if __name__ == "__main__":

    nr = InitNornir(config_file="config.yaml")
    eos = nr.filter(F(groups__contains="eos"))
    results = eos.run(task=file_copy, num_workers=10)
    print_result(results)


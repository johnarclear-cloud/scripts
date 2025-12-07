from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
import json
from rich import print as rprint
nr = InitNornir(config_file="config.yaml")


def new_random_test(task):
    configuration = task.run(
        task=netmiko_send_command,
        command_string="show configuration interfaces | display json",
    )
    dict_configuration = json.loads(configuration.result)
    interface = (dict_configuration["configuration"]["interfaces"]["interface"])
    for intf in interface:
        target = intf["name"]
        unit = intf["unit"]
        for element in unit:
            names = element["family"]["inet"]["address"]
            for name in names:
                ip = name["name"]
        print(f"{target} has an IP of {ip}")

result = nr.run(task=new_random_test)
# print_result(result)
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_pyez.plugins.tasks import pyez_facts

nr = InitNornir(config_file="config.yaml")

def get_some_data(task):
    facts =task.run(task=pyez_facts)
    version = (facts.result['version'])
    hostname = (facts.result['hostname'])
    print(f"the version of {hostname} is {version}")
result = nr.run(task=get_some_data)
#print_result(result)
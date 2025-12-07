from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_utils.plugins.functions import print_result
from nornir_pyez.plugins.tasks import pyez_get_config, pyez_config, pyez_commit,pyez_int_terse

nr = InitNornir(config_file="config.yaml")

snmp_config = """
snmp {
    community nor567;
    community nor890;
}
"""
#def test_stuff (task):
    #task.run(task=pyez_config, payload =snmp_config )
    #task.run(task=pyez_commit)

def get_some_data(task):
    #task.run(task=pyez_get_config)
    task.run(task=pyez_int_terse)
#result = nr.run(task=test_stuff)
result2 = nr.run(task=get_some_data)

#print_result(result)
print_result(result2)
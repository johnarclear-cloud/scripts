from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command

nr = InitNornir(config_file="config.yaml")

def get_running_interfaces():
    result=nr.run(task=netmiko_send_command, command_string="show interfaces terse")
    return result
from netmiko import ConnectHandler
from rich import print as rprint 
from inventory import DEVICES
import getpass

hostname = input("please enter the device IP: ")
username = input("please enter username: ")
mypass = getpass.getpass("please enter your super secret password: ")

with ConnectHandler(device_type="juniper", host=hostname, username=username, password=mypass, port=22) as conn:
    result = conn.send_command(command_string="show configuration")
    rprint(result)
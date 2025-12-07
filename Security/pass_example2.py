from netmiko import ConnectHandler
from rich import print as rprint 
from inventory import DEVICES
import getpass
import os


myuser = os.environ["MYUSERNAME"]
mypass = os.environ["MYPASSWORD"]

with ConnectHandler(device_type="juniper", host="192.168.68.201", username=myuser, password=mypass, port=22) as conn:
    result = conn.send_command(command_string="show configuration")
    rprint(result)
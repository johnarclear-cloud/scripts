#"THIS will do the following:
# import  script 3 which combines the host, group & default py data which we've named utils.py 
# it will then build the configuration using the templayte file found in templayes config.j2
# it wil lthen connect to the device and load that file using the local machine host variable 

import yaml
from inventory import DEVICES
from rich import print as rprint
from utils import load_vars
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
import os

def generate_config(device_vars):
    env = Environment(loader=FileSystemLoader("./templates"), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template("config.j2")
    configuration = template.render(device_vars)
    return configuration.splitlines()

def configure_junos(hostname, configuration):
    with ConnectHandler(
        device_type="juniper",
        host=hostname,
        username=os.environ["MYUSERNAME"],
        password=os.environ["MYPASSWORD"],
        port=22,
    ) as conn:
        result = conn.send_config_set(config_commands=configuration)
        print(result)

def main():
    for device in DEVICES:
        groups = device["groups"]
        hostname = device["hostname"]
        device_vars = load_vars(device, groups)
        configuration = generate_config(device_vars)
        configure_junos(hostname, configuration)
main()
#"THIS will do the following:
# import  script 3 which combines the host, group & default py data which we've named utils.py 
# it will then build the configuration using the templayte file found in templayes config.j2
# it wil lthen connect to the device and load that file using the local machine host variable datddd
# the from concurrent.futures import ThreadPoolExecutor will run the script at the same time "


from concurrent.futures import ThreadPoolExecutor
import yaml
from inventory import DEVICES
from rich import print as rprint
from utils import load_vars, generate_config, configure_junos

def main(device):
        groups = device["groups"]
        hostname = device["hostname"]
        device_vars = load_vars(device, groups)
        configuration = generate_config(device_vars)
        configure_junos(hostname, configuration)

with ThreadPoolExecutor() as execurtor:
        results = excecutor.map(main, DEVICES)
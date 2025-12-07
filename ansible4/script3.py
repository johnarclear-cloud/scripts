#!/usr/bin/python
from ansible.module_utils.basic import AnsibleModule
import json
from scrapli import Scrapli
from rich import print as rprint
from tabulate import tabulate
from itertools import zip_longest

def connect_junos(device_ip):
    my_device = {
        "platform": "juniper_junos",
        "host": device_ip,
        "auth_username": "john",
        "auth_password": "Juniper1",
        "auth_strict_key": False,
    }
    
    conn = Scrapli(**my_device)
    conn.open()
    result = conn.send_command("show configuration | display json")
    pretty_result = json.loads(result.result)
    return pretty_result

def parse_ospf(device_ip, pretty_result):
    print_list = []
    for area in pretty_result["configuration"]["protocols"]["ospf"]["area"]:
        area_name = area["name"]
        for interface in area["interface"]:
            interface_name = interface["name"]
            print_list.append(f"interface {interface_name} is in area {area_name}")
    table = zip_longest(print_list)
    return tabulate(table, headers=[f"{device_ip}"], tablefmt="psql")

pretty_result = connect_junos("192.168.68.201")
table_result = parse_ospf("192.168.68.201", pretty_result)
print(table_result)

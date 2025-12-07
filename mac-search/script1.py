import sys
from netaddr import EUI
from netaddr.core import AddrFormatError
from netmiko import ConnectHandler
from rich import print as rprint
import xmltodict
from inv import DEVICES

def validate_mac_address(target_mac):
    try:
        target_mac= EUI(target_mac)
        return target_mac
    except (ValueError, TypeError, AddrFormatError):
        print("invalid Mac address Entered")
        sys.exit(1)

def connect_junos_device(host, username, password):
    with ConnectHandler(
        device_type="juniper_junos",
        host=host,
        username=username,
        password=password,
        port=22,
    ) as conn:
        results = conn.send_command(command_string="show interfaces | display xml")
        structured_interface = xmltodict.parse(results)
        rprint(structured_interface)


def main():
    target_mac = input("enter the mac addresss you wish to target: ")
    target_mac = validate_mac_address(target_mac)
    for device in DEVICES:
        hostname = device["hostname"]
        host = device["host"]
        username = device["username"]
        password = device["password"]
        device_type = device["device_type"]
        if device_type == "juniper_junos":
            connect_junos_device(host=host,username=username,password=password)

if __name__ == "__main__":
    main()
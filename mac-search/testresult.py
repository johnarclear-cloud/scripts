import sys
from netaddr import EUI
from netaddr.core import AddrFormatError
from netmiko import ConnectHandler
from rich import print as rprint
import xmltodict
from inv import DEVICES
from pprint import pprint

def validate_mac_address(target_mac):
    try:
        target_mac= EUI(target_mac)
        return target_mac
    except (ValueError, TypeError, AddrFormatError):
        print("invalid Mac address Entered")
        sys.exit(1)
#Here we make sure the mac address is valid. 

def connect_junos_device(host,username,password):
    with ConnectHandler(
        device_type="juniper_junos",
        host=host,
        username=username,
        password=password,
        port=22,
    ) as conn:
        results = conn.send_command(command_string="show interfaces | display xml")
        structured_interface = xmltodict.parse(results)["rpc-reply"]["interface-information"]["physical-interface"]
        return structured_interface
#Here we connect to the device and full the interface RPC data out for the interfaces and stick in in to XML for parsing. 

def find_junos_mac(
        structured_interface,
        hostname,
        host,
        username,
        password,
        device_type,
        target_mac,
):
    dict_result = {}
    for interface in structured_interface:
        try: 
            mac_address = interface["current-physical-address"]
            name = interface["name"]
            if target_mac == mac_address:
                dict_result["local_interface"] = name
                dict_result["hostname"] = hostname
                dict_result["host"] = host
                dict_result["username"] = username
                dict_result["password"] = password
                dict_result["device_type"] = device_type

        except KeyError:
            pass
    return dict_result
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
            structured_interface = connect_junos_device(host=host,username=username,password=password)
            dict_result = find_junos_mac(
                structured_interface=structured_interface,
                hostname=hostname,
                host=host,
                username=username,
                password=password,
                target_mac=target_mac,
                device_type=device_type,
            )
        if dict_result:
           determine_device_type(dict_result, target_mac)

def determine_device_type(dict_result,target_mac):
    if dict_result["device_type"] == "juniper_junos":
       find_juniper_lldp(dict_result,target_mac)
    else:
        print("not today")

def find_juniper_lldp(dict_result, target_mac):
    hostname = dict_result["hostname"]
    local_interface = dict_result["local_interface"]
    host = dict_result["host"]
    username = dict_result["username"]
    password = dict_result["password"]

    rprint(f"[blue]{target_mac} found on {hostname}'s {local_interface}[/blue]")
    rprint(f"[yellow] Determining any potential connections....[/yellow]")

    with ConnectHandler(
        device_type="juniper_junos",
        host=host,
        username=username,
        password=password,
        port=22,
    ) as conn:
        result = conn.send_command(command_string="show lldp neighbors | display xml")
        has_remote_connections = False
        structured_interface = xmltodict.parse(result)
        for interface in structured_interface["rpc-reply"]["lldp-neighbors-information"]["lldp-neighbor-information"]:
            local_intf = interface["lldp-local-port-id"]
            if local_intf == local_interface:
                remote_intf = interface["lldp-remote-port-id"]
                remote_hostname = interface ["lldp-remote-system-name"]
                print(f"{local_interface} is connected to {remote_hostname}'s {remote_intf}")
                has_remote_connections = True
        if not has_remote_connections:
                print("Looks like nothing is connected here!")
                return
    


if __name__ == "__main__":
    main()
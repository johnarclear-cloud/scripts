from netmiko import ConnectHandler
import xmltodict
from rich import print as rprint
from inv import DEVICES

def connect_junos_device(host: str, username: str, password: str,) -> str:

    with ConnectHandler(
        device_type="juniper_junos",
        host=host,
        username=username,
        password=password,
        port=22,
    ) as conn:
        interfaces_xml = conn.send_command(
            command_string="show configuration interfaces | display xml"
        )
        return interfaces_xml
    
def parse_junos(hostname: str, interfaces_xml: str) -> None:
    result_dict = xmltodict.parse(interfaces_xml)
    interfaces = result_dict["rpc-reply"]
    rprint(interfaces)

def main() -> None:
    for device in DEVICES:
        hostname = device["hostname"]
        host = device["host"]
        username = device["username"]
        password = device["password"]
        device_type = device["device_type"]
        if device_type == "juniper_junos":
            interfaces_xml = connect_junos_device(host=host,username=username, password=password)
            parse_junos(hostname, interfaces_xml)

if __name__ == "__main__":
    main()


#this will print out the XML data to JSON 

from jnpr.junos import Device 
from jnpr.junos.exception import ConnectError
from rich import print as rprint 
import getpass
import sys
from lxml import etree
import xmltodict

#mypass = getpass.getpass()

device = Device(host="192.168.68.201", user="john", password="Juniper1")
try:
    device.open()
except ConnectError as err:
    print("connection to device failed")
    sys.exit(1)
except Exception as err:
    print(eer)
    sys.exit(1)

response = device.rpc.get_interface_information({"format": "json"})
#rprint(etree.tostring(response, pretty_print=True).decode())
#dict_result = xmltodict.parse(etree.tostring(response, pretty_print=True).decode())
#rprint(dict_result["interface-information"].keys())
rprint(response)
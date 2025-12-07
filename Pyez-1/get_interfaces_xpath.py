#tThis will peel out data through the use of Xpath to export the router id for example

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

response = device.rpc.get_ospf_overview_information()
hostname = device.rpc.get_system_information()
#rprint(etree.tostring(response, pretty_print=True).decode())
#dict_result = xmltodict.parse(etree.tostring(response, pretty_print=True).decode())
#rprint(dict_result["interface-information"].keys())
#rprint(etree.tostring(response, pretty_print=True).decode())
ospf_router_id = response.find(".//ospf-router-id").text
ospf_area = response.find(".//ospf-area").text
#rprint(etree.tostring(hostname, pretty_print=True).decode())
router_hostame = hostname.find(".//host-name").text
print(f" for {router_hostame}: The OSPF area for {ospf_router_id} is area {ospf_area}")
from netmiko import ConnectHandler 
from rich import print as rprint
import json
import pytest

def get_devices():
    devices = ["192.168.68.201","192.168.68.202"]
    return devices

@pytest.mark.parametrize("device", get_devices())
def test_bgp_state(device):
    conn = ConnectHandler(
        device_type="juniper_junos", 
        ip=device, 
        username="john", 
        password="Juniper1",
    )
    result = conn.send_command(command_string="show bgp neighbor | display json")
    dict_result = json.loads(result)

    # Get the list of neighbor dictionaries
    neighbor_list = dict_result["bgp-information"] 
    
    # Iterate through the list and print the desired key from each dictionary
    for neighbor in neighbor_list:
        state = (neighbor["bgp-peer"][0]["peer-state"][0]["data"])

        assert state == "Established", f"The state of the BGP connection is {state}"

from netmiko import ConnectHandler 
from rich import print as rprint
import json

def test_ospf_state():
    conn = ConnectHandler(
        device_type="juniper_junos", ip="192.168.68.201", username="john", password="Juniper1",
    )
    result = conn.send_command(command_string="show ospf neighbor | display json")
    dict_result = json.loads(result)

    # Get the list of neighbor dictionaries
    neighbor_list = dict_result["ospf-neighbor-information"] 
    
    # Iterate through the list and print the desired key from each dictionary
    for neighbor in neighbor_list:
        state = (neighbor["ospf-neighbor"][0]["ospf-neighbor-state"][0]["data"])

        assert state == "Full", f"The {state} state should be in the Full state"
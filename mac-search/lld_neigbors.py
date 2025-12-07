import sys
from netmiko import ConnectHandler
from rich import print as rprint
import xmltodict
from pprint import pprint
from inv import DEVICES 

def connect_and_find_lldp(host, username, password, hostname):
    """
    Connects to a Junos device and executes 'show lldp neighbors | display xml'.
    Parses the result and prints the local/remote connection details.
    """
    try:
        rprint(f"[bold cyan]Connecting to {hostname} ({host})...[/bold cyan]")
        with ConnectHandler(
            device_type="juniper_junos",
            host=host,
            username=username,
            password=password,
            port=22,
        ) as conn:
            # 1. Execute LLDP command and get XML output
            result = conn.send_command(command_string="show lldp neighbors | display xml")
            
            # 2. Parse the XML result
            structured_data = xmltodict.parse(result)
            
            # 3. Extract the list of neighbors, handling the single-neighbor case
            lldp_neighbors = structured_data["rpc-reply"]["lldp-neighbors-information"].get("lldp-neighbor-information")

            # Ensure lldp_neighbors is a list for iteration
            if lldp_neighbors is None:
                lldp_list = []
            elif isinstance(lldp_neighbors, dict):
                lldp_list = [lldp_neighbors]
            else:
                lldp_list = lldp_neighbors

            if not lldp_list:
                rprint(f"[yellow]  No LLDP neighbors found on {hostname}.[/yellow]")
                return

            rprint(f"[bold green]  Found {len(lldp_list)} neighbor(s):[/bold green]")
            print("-" * 50)
            print(f"{'Local Interface':<20} | {'Remote Hostname':<20} | {'Remote Interface':<15}")
            print("-" * 50)

            # 4. Iterate and print connection details
            for neighbor in lldp_list:
                local_intf = neighbor.get("lldp-local-port-id", "N/A")
                remote_hostname = neighbor.get("lldp-remote-system-name", "N/A")
                remote_intf = neighbor.get("lldp-remote-port-id", "N/A")
                
                print(f"{local_intf:<20} | {remote_hostname:<20} | {remote_intf:<15}")
            print("-" * 50)


    except Exception as e:
        rprint(f"[bold red]  Error connecting to or processing {hostname}: {e}[/bold red]")


def main():
   rprint("\n[bold magenta]Starting LLDP Discovery Across All Devices...[/bold magenta]")
   
   for device in DEVICES:
        hostname = device["hostname"]
        host = device["host"]
        username = device["username"]
        password = device["password"]
        device_type = device.get("device_type") # Use .get() for safety

        if device_type == "juniper_junos":
            connect_and_find_lldp(
                host=host,
                username=username,
                password=password,
                hostname=hostname,
            )
        else:
            rprint(f"[yellow]Skipping {hostname}: Device type '{device_type}' not supported for LLDP lookup.[/yellow]")
            
   rprint("[bold magenta]LLDP Discovery Complete.[/bold magenta]\n")


if __name__ == "__main__":
    main()
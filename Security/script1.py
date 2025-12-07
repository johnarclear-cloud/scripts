from napalm import get_network_driver
from rich import print as rprint

juniper_device = get_network_driver("junos")

with juniper_device(hostname="192.168.68.202", username="john", password="Juniper1") as conn:
      conn.load_replace_candidate(file="`R2.cfg")
      conn.commit_config(revert_in=60)
      print(conn.has_pending_commit())
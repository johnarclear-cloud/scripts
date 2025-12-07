import yaml
from rich import print as rprint 

my_data = yaml.safe_load(open("hosts.yaml"))
hosts = my_data["host"]
for host in hosts:
  print(host)
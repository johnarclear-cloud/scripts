from genie.testbed import load
from rich import print as rprint


testbed = load("my_testbed.yaml")

dev1 = testbed.devices["r1.jcs"]
dev1.connect(log_stdout=False)
result = dev1.parse("show version")
rprint(result["software-information"]["junos-version"])
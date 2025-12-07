from genie.testbed import load
from rich import print as rprint

testbed = load("my_testbed.yaml")


device_r1 = testbed.devices["r1.jcs"]
device_r1.connect(log_stdout=False)
terse_intf = device_r1.parse("show interfaces terse")
#rprint(terse_intf["fxp0.0"]["protocol"]["inet"])
ntp_config = device_r1.learn("ntp")
rprint(ntp_config.to_dict())
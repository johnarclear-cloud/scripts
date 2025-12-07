from genie.testbed import load
from rich import print as rprint
from pyats.async_ import pcall

def get_interface_test(dev):
    ntp_config = dev.learn("ntp["status"]")
    rprint(interface_result)

testbed = load("my_testbed.yaml")
testbed.connect(log_stdout=False)
results = pcall(get_interface_test, dev=testbed.devices.values())
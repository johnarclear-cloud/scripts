#tThis will peel out data through the use of Xpath to export the router id for example

from jnpr.junos import Device 
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import ConnectError
from rich import print as rprint 
import getpass
import sys

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

config = Config(device)
bgp_config = """
protocols {
bgp {
    description "this is for r1";
    local-as 65001;
    }
}
"""
config.lock()
config.load(bgp_config)
config.pdiff()
if config.commit_check() == True:
    config.commit()
else:
    config.rollback()
config.unlock
device.close()
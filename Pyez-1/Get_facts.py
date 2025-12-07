#this will pump out the device facts kets and show the version & serial as example
from jnpr.junos import Device 
from jnpr.junos.exception import ConnectError
from rich import print as rprint 
import getpass


mypass = getpass.getpass()

device = Device(host="192.168.68.201", user="john", password=mypass)
try:
    device.open()
except ConnectError as err:
    print("connection to device failed")
    sys.exit(1)
except Exception as err:
    print(eer)
    sys.exit(1)
    

response = device.facts
rprint(response.keys())
print(f"The Device version is {response['version']}")
print(f"The Device serial is {response['serialnumber']}")
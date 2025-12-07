import requests 
from rich import print as rprint 

url = "http://192.168.68.101:5050"

def get_networks():
    response = requests.get(f"{url}/networks")
    return response.json()
#rprint(response["networks"]):
#for output in response["networks"]:
#    print(output["subnets"])
def get_network(id):
    response = requests.get(f"{url}/network/{id}")
    if response.status_code == 404:
        raise ValueError(response.json()["error"])
    return response.json()

response = get_network(2)
rprint(response)
    
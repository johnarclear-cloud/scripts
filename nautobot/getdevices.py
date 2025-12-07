import requests
from rich import print as rprint

URL = "https://192.168.68.103/api/dcim/devices"

headers = {"Authorization": "token e923fb9e6a13e41ab4a8de9a95f023b18c305547"}

response = requests.get(URL, headers=headers, verify=False)
rprint(response)
rprint(response.json())
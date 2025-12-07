import json
import requests
from rich import print as rprint

BASE_URL = "http://192.168.68.201:8080/rpc"

endpoint = "/get-ospf-interface-information"
credentials = ("john", "Juniper1")

headers = {"Accept": "application/json"}

try:
    response = requests.post(BASE_URL + endpoint, auth=credentials, headers=headers)
    rprint(response.text)



except requests.exceptions.RequestException as err:
    rprint(f"ERROR: {err}")

except Exception as e:
    rprint(f"ERROR: {e}")
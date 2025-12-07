import json
import requests
from rich import print as rprint
import httpx

BASE_URL = "http://192.168.68.201:8080/rpc"

endpoint = "/get-snmp-information"
credentials = ("john", "Juniper1")
headers = {"Accept": "application/json"}

try:
    with httpx.Client() as client:
        response = client.post(BASE_URL + endpoint, auth=credentials, headers=headers)
        response.raise_for_status()
        rprint(json.loads(response.text))



except httpx.HTTPError as err:
    rprint(f"ERROR: {err}")

except httpx.ConnectTimeout as e:
    rprint(f"ERROR: {e}")
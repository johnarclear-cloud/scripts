import json
import requests
from rich import print as rprint

BASE_URL = "http://192.168.68.201:8080/rpc"

endpoint = "/get-system-users-information"
credentials = ("john", "Juniper1")

headers = {"Accept": "application/json"}

try:
    response = requests.get(BASE_URL + endpoint, auth=credentials, headers=headers)
    dict_response = response.json()
    rprint(dict_response["system-users-information"][0]["uptime-information"][0]["date-time"])



except requests.exceptions.RequestException as err:
    rprint(f"ERROR: {err}")

except Exception as e:
    rprint(f"ERROR: {e}")
import requests
from rich import print as rprint

query = """
query {
      devices {
        id
        name
        interfaces {
          name
          ip_addresses {
            address
          }
        }
      }
    }
"""
payload = {"query": query}

URL = "https://192.168.68.103/api/graphql/"

headers = {
    "Authorization": "token e923fb9e6a13e41ab4a8de9a95f023b18c305547",
    "Content-Type": "application/json",
    }

response = requests.post(URL, headers=headers, verify=False, json = payload)
rprint(response)
dict_response = response.json()
devices = (dict_response["data"]["devices"])
for device in devices:
    rprint(device["name")

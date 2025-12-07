import requests
from rich import print as rprint

URL = "https://192.168.68.103/api/dcim/devices"

headers = {"Authorization": "token e923fb9e6a13e41ab4a8de9a95f023b18c305547"}

payload = {
    "name": "R3",
    "device_type": "cac6878b-f63c-4107-b67c-014708dfaf16",
    "role": "7ec6016a-d3a3-4ca3-947e-995bbf037528",
    "location": "9ed75ed6-7e31-4ef0-8ec3-14c4121a24db",
    "status": "fb80616e-d666-483b-b033-86003efe883b",
    "platform": "362ff1ca-66e3-4371-91e6-565b54a25a80",
    "tenant": "1d50594c-0202-4cc1-ba79-deb496a65251",
}

response = requests.post(URL, headers=headers, verify=False, json=payload)
rprint(response)
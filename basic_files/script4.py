from scrapli import Scrapli

my_device = {
  "platform": "juniper_junos",
  "host": "192.168.68.202",
  "auth_username": "john",
  "auth_password": "Juniper1",
  "auth_strict_key": False,
}

conn = Scrapli(**my_device)
conn.open()
result = conn.send_configs_from_file(file="R2.cfg")
print(result.result)
conn.close()
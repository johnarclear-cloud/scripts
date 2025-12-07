from netmiko import ConnectHandler

my_device = {
  "device_type": "juniper",
  "host": "192.168.68.201",
  "username": "john",
  "password": "Juniper1",
  "port": 22,
}

conn = ConnectHandler(**my_device)
my_list_of_configs = [
  "set system host-name R1",
  "commit"
  ]
result = conn.send_config_set(config_commands=my_list_of_configs)
print(result)
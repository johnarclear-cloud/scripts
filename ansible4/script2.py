from scrapli import Scrapli

def connect_junos(device_ip):

    my_device = {
        "platform": "juniper_junos",
        "host": device_ip,
        "auth_username": "john",
        "auth_password": "Juniper1",
        "auth_strict_key": False,
    }
    
    conn = Scrapli(**my_device)
    conn.open()
    result = conn.send_command("show configuration")
    return result.result

result = connect_junos("192.168.68.201")
print(result)
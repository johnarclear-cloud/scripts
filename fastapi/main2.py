from yaml import safe_load
from fastapi import FastAPI
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command
from nornir_logic import get_running_devices

nr = InitNornir(config_file="config.yaml")

app = FastAPI()


@app.get("/")
def root() -> dict:
    """
    Root page for application
    
    :return: A Simple greeting message
    """
    return {"Hello": "World"}

@app.get("/inventory")
async def get_devices():
    return nr.inventory.hosts

@app.get("/all")
async def get_all_vars() -> dict:
    """
    Get all the variables within the ALL group
    
    :return: Dictionary of all the variables within the YAML file
    """
    with open("group_vars/all.yaml", encoding="utf-8") as file:
        all_vars=safe_load(file)
    return {"all": all_vars}

@app.get("/devinfo")
async def get_all_info() -> dict:
    """
    Get all the host information for Nornir host yaml file
    
    :return: Dictionary of all the varibales wirhin the yaml file
    """
    with open("hosts.yaml", encoding="utf-8") as file:
        info_data=safe_load(file)
    return {"info": info_data}




#@app.get("/configuration", tags =["configs"])
#async def get_all_configs():
#    result = nr.run(task=netmiko_send_command, command_string="show configuration")
#    return result
#
#@app.get("/interfaces", tags =["configs"])
#async def get_all_interface():
#    result = nr.run(task=netmiko_send_command, command_string="show interface terse")
#    return result
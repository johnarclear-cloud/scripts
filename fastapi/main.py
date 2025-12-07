from yaml import safe_load
from fastapi import FastAPI, Request
from get_interface import get_running_interfaces
from fastapi.templating import Jinja2Templates
from get_device_config import get_running_devices
from get_bgp import get_running_bgp
from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command

nr = InitNornir(config_file="config.yaml")
app = FastAPI()
templates = Jinja2Templates(directory="templates")


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


@app.get("/get-running")
async def get_running(request: Request):
    result = get_running_devices()
    return templates.TemplateResponse("output-config.html", {"request": request, "output": result}
    )

@app.get("/get-interfaces")
async def get_interfaces(request: Request):
    result = get_running_interfaces()
    return templates.TemplateResponse("output.html", {"request": request, "output": result}
    )

@app.get("/get-bgp")
async def get_bgp(request: Request):
    result = get_running_bgp()
    return templates.TemplateResponse("output.html", {"request": request, "output": result}
    )

@app.get("/get-bgp/{hostname}")
async def get_bgp(request: Request,hostname):
    device = nr.filter(device_name=f"{hostname}")
    bgp =  device.run(netmiko_send_command, command_string=f"show bgp summary")
    return templates.TemplateResponse("output.html", {"request": request, "output": bgp})
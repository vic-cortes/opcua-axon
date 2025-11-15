import requests

from config import IgnitionConfig


# http://localhost:8088/data/api/v1/resources/names/com.inductiveautomation.opcua/device
class IgnitionUrls:
    GET_DEVICES_NAMES = f"{IgnitionConfig.API_V1_BASE_URL}/resources/names/com.inductiveautomation.opcua/device"


headers = {"X-Ignition-API-Token": IgnitionConfig.API_KEY}

response = requests.get(IgnitionUrls.GET_DEVICES_NAMES, headers=headers)

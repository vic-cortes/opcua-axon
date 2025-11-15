import requests

from config import IgnitionConfig


# http://localhost:8088/data/api/v1/resources/names/com.inductiveautomation.opcua/device
class IgnitionUrls:
    GET_DEVICES_NAMES = f"{IgnitionConfig.API_V1_BASE_URL}/resources/names/com.inductiveautomation.opcua/device"
    LIST_SCHEDULE_RESOURCES = (
        f"{IgnitionConfig.API_V1_BASE_URL}/resources/list/ignition/schedule"
    )
    GATEWAY_INFO = f"{IgnitionConfig.API_V1_BASE_URL}/gateway-info"
    SCAN_PROJECTS = f"{IgnitionConfig.API_V1_BASE_URL}/scan/projects"


headers = {"X-Ignition-API-Token": IgnitionConfig.API_KEY}

response = requests.get(IgnitionUrls.SCAN_PROJECTS, headers=headers)

print("Status Code:", response.status_code)

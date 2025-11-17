import requests

from config import IgnitionConfig

# http://localhost:8088/data/api/v1/resources/names/com.inductiveautomation.opcua/device

SERVER_ID = "Sample_Tags"


class IgnitionUrls:
    GET_DEVICES_NAMES = f"{IgnitionConfig.API_V1_BASE_URL}/resources/names/com.inductiveautomation.opcua/device"
    REMOTE_TAG_PROVIDERS = f"{IgnitionConfig.API_V1_BASE_URL}/gateway-network/remote-tag-providers/{SERVER_ID}"
    GET_TAG_PROVIDERS = (
        f"{IgnitionConfig.API_V1_BASE_URL}/resources/names/ignition/tag-provider"
    )
    LIST_SCHEDULE_RESOURCES = (
        f"{IgnitionConfig.API_V1_BASE_URL}/resources/list/ignition/schedule"
    )
    GATEWAY_INFO = f"{IgnitionConfig.API_V1_BASE_URL}/gateway-info"
    SCAN_PROJECTS = f"{IgnitionConfig.API_V1_BASE_URL}/scan/projects"
    GET_TAG_PROVIDERS_CONFIG = (
        f"{IgnitionConfig.API_V1_BASE_URL}/resources/find/ignition/tag-provider"
    )


headers = {"X-Ignition-API-Token": IgnitionConfig.API_KEY}
providers_name = "Sample_Device"
response = requests.get(
    IgnitionUrls.REMOTE_TAG_PROVIDERS,
    headers=headers,
)

print("Status Code:", response.text)

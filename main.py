import requests

from config import IgnitionConfig

# http://localhost:8088/data/api/v1/resources/names/com.inductiveautomation.opcua/device

SERVER_ID = "Ignition-a497227b8ad8"


class IgnitionUrls:
    GET_DEVICES_NAMES = f"{IgnitionConfig.API_V1_BASE_URL}/resources/names/com.inductiveautomation.opcua/device"
    GATEWAY_NAME = f"{IgnitionConfig.API_V1_BASE_URL}/overview/name"
    REMOTE_TAG_PROVIDERS = f"{IgnitionConfig.API_V1_BASE_URL}/gateway-network/remote-tag-providers/{SERVER_ID}"
    GET_TAG_PROVIDERS_NAMES = (
        f"{IgnitionConfig.API_V1_BASE_URL}/resources/names/ignition/tag-provider"
    )
    LIST_TAG_PROVIDERS_RESOURCES = (
        f"{IgnitionConfig.API_V1_BASE_URL}/resources/list/ignition/tag-provider"
    )
    LIST_SCHEDULE_RESOURCES = (
        f"{IgnitionConfig.API_V1_BASE_URL}/resources/list/ignition/schedule"
    )
    GATEWAY_INFO = f"{IgnitionConfig.API_V1_BASE_URL}/gateway-info"
    SCAN_PROJECTS = f"{IgnitionConfig.API_V1_BASE_URL}/scan/projects"
    GET_TAG_PROVIDERS_CONFIG = (
        f"{IgnitionConfig.API_V1_BASE_URL}/resources/find/ignition/tag-provider"
    )
    RUNNING_SCRIPTS = f"{IgnitionConfig.API_V1_BASE_URL}/scripts"
    LIST_ALL_PROJECTS = f"{IgnitionConfig.API_V1_BASE_URL}/projects/list"
    DESCRIBE_TAG_PROVIDERS_RESOURCE_TYPE = (
        f"{IgnitionConfig.API_V1_BASE_URL}/resources/type/ignition/tag-provider"
    )
    GET_SYNCABLE_ITEMS = f"{IgnitionConfig.API_V1_BASE_URL}/sync/items"
    LIST_OPC_CONNECTIONS_RESOURCES = (
        f"{IgnitionConfig.API_V1_BASE_URL}/resources/list/ignition/opc-connection"
    )


# https://docs.inductiveautomation.com/docs/8.3/ignition-modules/web-dev
PROJECT_NAME = "mabe_axon/axon/api"
BASE_CUSTOM_ENDPOINT = f"http://localhost:8088/system/webdev/{PROJECT_NAME}"


class CustomEndpoints:
    RAMP = f"{BASE_CUSTOM_ENDPOINT}/ramp"


headers = {"X-Ignition-API-Token": IgnitionConfig.API_KEY}
providers_name = "[Sample_Tags]Ramp/Ramp0"

response = requests.get(
    IgnitionUrls.LIST_OPC_CONNECTIONS_RESOURCES,
    headers=headers,
)
# response = requests.get(CustomEndpoints.RAMP, headers=headers)

if response.ok:
    print("Response JSON:", response.json())

print("Status Code:", response.text)

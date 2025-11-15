import os

from dotenv import load_dotenv

load_dotenv(override=True)


class IgnitionConfig:
    API_KEY = os.getenv("IGNITION_API_KEY")
    API_V1_BASE_URL = "http://localhost:8088/api/v1"

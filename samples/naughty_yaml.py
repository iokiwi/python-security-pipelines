import yaml
from typing import Dict

def deserialise_service_config(config: str) -> Dict:
    try:
        return yaml.load(config)
    except:
        print("An error occurred")

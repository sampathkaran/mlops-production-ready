# Here we define the user defined function that we frequenlty we call in the code
import os
import yaml
from us_visa.exception import UsVisaException

# Read YAML file function

def read_yaml(file_path:str) -> dict:
    try:
        with open (file_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise UsVisaException(e) from e

# Write YAML file function 

def write_yaml(file_path:str, content, replace:bool = False) -> None:
    try:
        # if the replace is True is below block will be executed
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        # This command below will sepeate directory from file path
        dir = os.path.dirname(file_path)
        os.makedirs(dir, exist_ok=True)
        with open(file_path, 'w') as f:
            return yaml.dump(content, f)
    except Exception as e:
        raise UsVisaException(e) from e



# from us_visa.logger import logging

# logging.info("Hello from logger")

# from us_visa.exception import UsVisaException

# try:
#     2/0
# except Exception as error:
#     raise UsVisaException(error)
import yaml
from us_visa.utils.main_util import read_yaml, write_yaml

# print(read_yaml("/home/sam/my-study/mlops-production-ready/test.yaml"))

names_yaml = """
- 'eric'
- 'justin'
- 'mary-kate'
"""
names = yaml.safe_load(names_yaml)
print(names)
print(type(names))
write_yaml("/home/sam/my-study/mlops-production-ready/test.yaml", names, replace=False)
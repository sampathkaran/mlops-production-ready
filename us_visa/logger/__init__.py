# ref - https://github.com/aymanejaz/End-To-End-Data-Science-Project

# Create custom logger 
import logging

# To manage files and directories
import os

from datetime import datetime
filename = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

directory = "logs"

os.makedirs(directory, exist_ok=True)

filepath = os.path.join(directory, filename)

logging.basicConfig(filename = filepath, level=logging.DEBUG, format="%(asctime)s:%(name)s:%(levelname)s:%(message)s")
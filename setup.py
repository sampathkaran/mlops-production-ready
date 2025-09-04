#It lets you install your project using pip install .
from setuptools import setup, find_packages
setup(
    name = "us_visa",
    version = "0.0.0.0",
    author = "sam",
    author_email= "john_doe@gmail.com",
    packages=find_packages() # it will look for init.py file and consider the folder as a package
)
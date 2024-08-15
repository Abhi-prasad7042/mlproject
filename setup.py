from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str)->List[str]:
    req = []
    with open(file_path, "r") as f:
        req = f.readlines()
        req = [r.replace("\n","") for r in req]
    return req[:-1]


setup(name="mlproject",
version="0.0.1",
author="abhi",
author_email="abhiprasad7042@gmail.com",
packages=find_packages(),
install_requires= get_requirements("requirements.txt")
)
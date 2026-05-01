from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []

    with open(file_path, 'r') as file:
        for line in file:
            package = line.strip()

            # Skip empty lines
            if not package:
                continue

            # Skip editable install
            if package.startswith('-e .'):
                continue

            # Skip comments
            if package.startswith('#'):
                continue

            # Skip other flags (optional)
            if package.startswith('-'):
                continue

            requirements.append(package)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Zeno Land",
    author_email="pavan.c.desai@gmail.com",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=get_requirements("requirements.txt"),
)
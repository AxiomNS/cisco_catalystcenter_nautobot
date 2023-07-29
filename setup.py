from os import path
from setuptools import setup, find_packages


with open("requirements.txt") as f:
    requirements = f.read().splitlines()
with open(
    path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8"
) as f:
    long_description = f.read()

PACKAGE_KEYWORDS = [
    "cisco",
    "dna",
    "dnacenter",
    "python",
    "api",
    "catalystcenter",
    "catalyst",
    "sdk",
    "nautobot",
]

setup(
    name="ciscodnacnetbox",
    version="3.2.1",
    description="Cisco Catalyst Center Integration with Nautobot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AxiomNS/cisco_catalystcenter_nautobot",
    author="Chris Preston",
    author_email="chris.preston@axiomns.com",
    license="CISCO SAMPLE CODE LICENSE",
    install_requires=requirements,
    packages=find_packages(exclude=["img", "dev"]),
    include_package_data=True,
    python_requires=">=3.3",
    zip_safe=False,
)

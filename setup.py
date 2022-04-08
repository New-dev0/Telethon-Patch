import setuptools
from telethonpatch import __version__, __author__


with open("README.md", "r") as readme:
    long_description = readme.read()


setuptools.setup(
    name= "telethon-patch",
    version=__version__,
    long_description=long_description,
    author=__author__,
    author_email="New-dev0@outlook.com",
    url="https://github.com/New-dev0/Telethon-Patch",
    packages=setuptools.find_packages(),
    install_requires=["Telethon@https://github.com/Telethon-Fork/Telethon/archive/main.zip"],
    ext_package=["scripts", "data"] 
)
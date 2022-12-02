import setuptools
from telethonpatch import __version__, __author__


with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()


setuptools.setup(
    name="telethon-patch",
    version=__version__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNUV3",
    author=__author__,
    author_email="New-dev0@outlook.com",
    url="https://github.com/New-dev0/Telethon-Patch",
    packages=setuptools.find_packages(),
    install_requires=["Telethon"],
    keywords=["telethon", "telethon-patch", "telegram", "mtproto"],
    ext_package=["scripts", "data", "examples"],
    classifiers=[
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    "Operating System :: OS Independent",
]
)

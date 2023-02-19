import setuptools, re

with open("telethonpatch/__init__.py", "rt", encoding="utf8") as version:
    version = re.search(r'__version__ = "(.*?)"', version.read())[1]

with open("telethonpatch/__init__.py", "rt", encoding="utf8") as author:
    author = re.search(r'__author__ = "(.*?)"', author.read())[1]


with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()


setuptools.setup(
    name="telethon-patch",
    version=version,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GNUV3",
    author=author,
    author_email="New-dev0@outlook.com",
    url="https://github.com/New-dev0/Telethon-Patch",
    packages=setuptools.find_packages(),
    install_requires=["Telethon@https://github.com/LonamiWebs/Telethon/archive/v1.zip"],
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

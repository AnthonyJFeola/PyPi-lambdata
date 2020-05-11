from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambdata-AnthonyJFeola", # the name that you will install via pip
    version="2.0",
    author="Anthony J Feola",
    author_email="anthonyfeola18@gmail.com",
    description="Hyperlink removal tool",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/AnthonyJFeola/lambdata-AnthonyJFeola",
    #keywords="",
    packages=find_packages() # ["my_lambdata"]
)
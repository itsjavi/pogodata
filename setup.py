from setuptools import setup

version = "0.5.4"

setup(
    name="pogodata",
    author="ccev",
    url="https://github.com/ccev/pogodata",
    version=version,
    install_requires=["requests"],
    packages=["pogodata"],
    long_description="For documentation, please visit https://github.com/ccev/pogodata",
    description="Easy and up-to-date Pogo Data"
)

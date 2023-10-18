from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in intech/__init__.py
from intech import __version__ as version

setup(
	name="intech",
	version=version,
	description="Ecommerce App",
	author="khan",
	author_email="khanmomodou11@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

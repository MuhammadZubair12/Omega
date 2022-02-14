from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in omega/__init__.py
from omega import __version__ as version

setup(
	name="omega",
	version=version,
	description="For erpnext customization",
	author="Muhammad Zubair",
	author_email="zubairmazhar23@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

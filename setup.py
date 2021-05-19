from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in webapp/__init__.py
from webapp import __version__ as version

setup(
	name='webapp',
	version=version,
	description='Front-end for NextERP.mn',
	author='Manduul B.',
	author_email='manduul@hello.mn',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

"""Setup script for Kevin's randomunser.me API wrapper"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, 'README.md')) as fid:
    README = fid.read()

# Required dependencies
dependencies = []

# Call to setup()
setup(
    name='randomuserapi',
    version='1.1.0',
    description='API Wrapper for randomuser.me api',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Kevin Beacham',
    author_email='kevinwbeacham@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.12',
    ],
    install_requires=dependencies
)
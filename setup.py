from pathlib import Path
from importlib_metadata import entry_points
from setuptools import setup

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1'
DESCRIPTION = 'Description'
PACKAGE_NAME = 'package_cf'
AUTHOR = ''
EMAIL = ''
GITHUB_URL = ''

setup(
    name = PACKAGE_NAME,
    packages = [PACKAGE_NAME],
    entry_points = [
        "console_scripts":
            # Cuando alguien instale el paquete y ejecute el comando py_pk_cf, se ejecutara el resto de la linea , es decir, el comando
            ["py_pk_cf=package_cf.__main__:main"]
    ],
    version = VERSION,
    license='MIT',
    description = DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    author = AUTHOR,
    author_email = EMAIL,
    url = GITHUB_URL,
    keywords = [],
    install_requires=[ 
        'requests',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
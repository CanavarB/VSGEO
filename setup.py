from setuptools import find_packages, setup


setup(
    name="VSGEO",
    version="1.0.0-beta",
    description="VSCO OSINT",
    author="Canavar B.",
    packages=find_packages(),
    url="https://github.com/mvabdi/vsco-scraper",
    entry_points={
        'console_scripts':[
            'vsgeo=src.main:main',
        ],
    },
    keywords="vsco osint",
)

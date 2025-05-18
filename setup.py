# File: setup.py
from setuptools import setup, find_packages

setup(
    name="vulnguard-core",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "ollama>=0.1.2",
        "fpdf2>=2.7.5",
        "pyyaml>=6.0",
        "python-dotenv>=1.0.0"
    ],
    entry_points={
        "console_scripts": [
            "vulnguard-core=sec_analyzer.cli:main"
        ]
    },
    package_data={
        "sec_analyzer": ["config/*.yaml", "config/*.json"]
    },
    python_requires=">=3.8",
)
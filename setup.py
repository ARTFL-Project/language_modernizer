"""Simple package to install the language_modernizer package"""

from setuptools import setup

setup(
    name="language_modernizer",
    version="0.1",
    description="Modernize words in different languages",
    author="Clovis Gladstone",
    author_email="clovisgladstone@uchicago.edu",
    packages=["language_modernizer", "language_modernizer.lang"],
)

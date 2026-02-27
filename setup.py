from setuptools import setup, find_packages

def requrements():
    with open('requirements.txt', 'r') as f:
        return f.read().splitlines()

setup(
    name='placement_prediction',
    version='0.1.0',
    packages=find_packages(),
    install_requires=requrements(),
    description='A package for predicting placement outcomes using machine learning models.',
    author='omkar kamate',
    author_email="omkarkamate2004@gmail.com"
)
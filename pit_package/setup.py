from setuptools import setup, find_packages


setup(
    name='pit_poland',
    version='1.0',
    packages=find_packages(),
    license='BSD 2-clause',
    author='Jakub Bandurski',
    author_email='j.bandurski@student.uw.edu.pl',
    description='Package calculates PIT statistics for Poland',
    install_requires=["pandas", "numpy", "matplotlib", "openpyxl", "xlrd"]
)
from setuptools import setup


setup(
    name='NYPD_zal',
    version='1.0',
    packages=['pit_poland', 'pit_poland.analysis', 'pit_poland.data_export', 'pit_poland.data_import'],
    url='',
    license='BSD 2-clause',
    author='Jakub Bandurski',
    author_email='j.bandurski@student.uw.edu.pl',
    description='Package calculates PIT statistics for Poland',
    install_requires=["pandas", "matplotlib", "openpyxl", "xlrd"]
)

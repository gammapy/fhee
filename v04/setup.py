from setuptools import setup

setup(
    name='fhee',
    version=1.0,
    description='Fermi high-energy explorer',
    url='https://github.com/gammapy/fhee',
    packages=['fhee', 'fhee.tests'],
    install_requires=['numpy', 'astropy'],
    package_data={
        'fhee': ['data/*'],
    },
)

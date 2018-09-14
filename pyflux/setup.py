
from setuptools import setup

setup_args = dict (
    name="pyflux",
    version="0.9",
    description= 'A Python Client for fluxlang',
    license='MIT',
    url='https://github.com/enthusiasm-foundation/pyflux',
    author='PyFlux Mafia',
    author_email='gianarb@influxdata.com',
    packages=[ "./" ],
    install_requires = [ 'setuptools',
                         'pandas',
                         'json2html',
                         'requests',
                         'matplotlib',
                         'pygments'
    ])


if __name__ == '__main__':
    setup( **setup_args )
from setuptools import setup, find_packages
setup (
    name='converter',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'click'
    ],
    entry_points='''
    [console_scripts]
    convert=converter:converter
    nearc=converter:near
    '''
)
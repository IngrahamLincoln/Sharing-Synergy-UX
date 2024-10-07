from setuptools import setup

setup(
    name='sharing_synergy',
    version='1.0.1',
    packages=['sharing_synergy'],
    entry_points={
        'console_scripts': [
            'syn = sharing_synergy.main:main',
        ],
    },
)
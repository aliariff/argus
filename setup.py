from setuptools import setup

setup(
    name='argus',
    version='0.1',
    py_modules=['argus'],
    entry_points='''
        [console_scripts]
        argus=argus:cli
    ''',
)

from setuptools import setup

setup(
    name='argus',
    version='0.1',
    py_modules=['argus'],
    install_requires=[
        'Click==6.7',
        'requests==2.19.1',
		'beautifulsoup4==4.6.3',
		'tqdm==4.25.0'
    ],
    entry_points='''
        [console_scripts]
        argus=argus:cli
    ''',
)

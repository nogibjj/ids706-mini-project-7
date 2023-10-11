from setuptools import setup, find_packages

setup(
    name="my_tool",
    version="0.1",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'my_tool=my_tool.main:main',
        ],
    },
    install_requires=[
        'mysql-connector-python'
    ],
)

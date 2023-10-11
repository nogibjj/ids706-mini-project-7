from setuptools import setup, find_packages

setup(
    name="my_tool",
    version="0.1",
    description="A command-line tool to interact with a MySQL database",
    author="Gunel Aghakishiyeva",
    url="https://github.com/nogibjj/ids706-mini-project-7",
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

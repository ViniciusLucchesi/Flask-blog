from setuptools import setup

setup(
    name = 'flask_blog',
    author = 'Vinicius Lucchesi',
    version = '0.1.0',
    packages = ['blog'],
    install_requires = [
        'flask',
        'flask-pymongo',
        'dynaconf',
        'mistune',
        'python-slugify',
        'flask-simplelogin',
    ]
)
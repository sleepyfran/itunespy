from setuptools import setup
from pathlib import Path

root_dir = Path(__file__).parent
long_description = (root_dir/"README.md").read_text()

setup(
    name='itunespy',
    version='1.6.1',
    description='A simple library to fetch data from the iTunes Store API made for Python 3.X',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Fran González (@sleepyfran)',
    author_email='fgzv@outlook.com',
    url='http://github.com/sleepyfran/itunespy',
    packages=['itunespy'],
    install_requires=['requests>=2.8', 'pycountry>=19.8'],
    extras_require={
        'dev': ['mypy', 'types-requests']
    },
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)

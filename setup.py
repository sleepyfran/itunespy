from setuptools import setup

setup(
    name='itunespy',
    version='1.6.0',
    description='A simple library to fetch data from the iTunes Store API made for Python 3.X',
    author='Fran González (@spaceisstrange)',
    author_email='fgonzaleva@gmail.com',
    url='http://github.com/spaceisstrange/itunespy',
    packages=['itunespy'],
    install_requires=['requests>=2.8', 'pycountry>=19.8'],
    extras_require={
        'dev': ['mypy']
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

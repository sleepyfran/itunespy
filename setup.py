from setuptools import setup

setup(
    name='itunespy',
    version='1.5.5',
    description='A simple library to fetch data from the iTunes Store API made for Python 3.X',
    author='Fran González (@spaceisstrange)',
    author_email='fgonzaleva@gmail.com',
    url='http://github.com/spaceisstrange/itunespy',
    packages=['itunespy'],
    install_requires=['requests>=2.8'],
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)

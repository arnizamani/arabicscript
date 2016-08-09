#!/usr/bin/python
from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='arabicscript',
    version='0.1',
    description='Tools for Arabic script',
    long_description=readme(),
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Text Processing :: Linguistic',],
    keywords=['Arabic script Unicode text'],
    url='https://github.com/arnizamani/arabicscript',
    author='Abdul Rahim Nizamani',
    author_email='abdulrahimnizamani@gmail.com',
    license='GPL',
    packages=['arabicscript'],
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    test_suite = 'nose.collector',
    tests_require = ['nose']
)

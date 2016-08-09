#!/usr/bin/python
from setuptools import setup

package_name = 'arabicscript'
current_version = '0.1.1'
development_status = 'Development Status :: 2 - Pre-Alpha'

author_name = 'Abdul Rahim Nizamani'
author_email = 'abdulrahimnizamani@gmail.com'
package_url = 'https://github.com/arnizamani/arabicscript'


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name=package_name ,
    version=current_version,
    description='Tools for Arabic script',
    long_description=readme(),
    classifiers=[development_status,
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Programming Language :: Python :: 3.5',
                 'Topic :: Text Processing :: Linguistic',],
    keywords=['Arabic', 'writing script', 'Unicode', 'text processing'],
    url=package_url,
    author=author_name,
    author_email=author_email,
    license='GPL',
    packages=['arabicscript'],
    include_package_data=True,
    install_requires=[],
    zip_safe=False,
    test_suite = 'nose.collector',
    tests_require = ['nose']
)

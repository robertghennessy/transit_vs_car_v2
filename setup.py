#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Robert G Hennessy",
    author_email='robertghennessy@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Compare travel time of public transit to car.",
    entry_points={
        'console_scripts': [
            'transit_vs_car_v2=transit_vs_car_v2.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='transit_vs_car_v2',
    name='transit_vs_car_v2',
    packages=find_packages(include=['transit_vs_car_v2', 'transit_vs_car_v2.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/robertghennessy/transit_vs_car_v2',
    version='0.1.0',
    zip_safe=False,
)

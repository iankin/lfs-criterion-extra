# -*- coding: utf-8 -
#
# This file is part of speedydeploy released under the MIT license. 
# See the NOTICE for more information.

import os
import sys
from setuptools import setup, find_packages

from lfs_criterion_extra import VERSION


setup(
    name='lfs_criterion_extra',
    version=VERSION,

    description='Extra critetions for LFS',
    long_description=file(
        os.path.join(
            os.path.dirname(__file__),
            'README.md'
        )
    ).read(),
    author='Victor Safronovich',
    author_email='vsafronovich@gmail.com',
    license='MIT',
    url='http://github.com/suvit/lfs-criterion-extra',
    zip_safe=False,
    packages=find_packages(exclude=['docs', 'examples', 'tests']),
    install_requires=file(
        os.path.join(
            os.path.dirname(__file__),
            'requirements.txt'
        )
    ).read().split(),
    include_package_data=True,
)

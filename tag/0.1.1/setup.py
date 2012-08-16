#!/usr/bin/env python
#
# Setup prog for cacheschedconfig
#
#
release_version='0.1.1'

import re
import sys
import commands
from distutils.core import setup
from distutils.command.install import install as install_org
from distutils.command.install_data import install_data as install_data_org

        
# setup for distutils
setup(
    name="panda-cacheschedconfig",
    version=release_version,
    description='panda-cacheschedconfig package',
    long_description='''This package contains cacheschedconfig''',
    license='GPL',
    author='Panda Team',
    author_email='hn-atlas-panda-pathena@cern.ch',
    maintainer='Graeme Stewart',
    maintainer_email='graeme.andrew.stewart@cern.ch',
    url='https://twiki.cern.ch/twiki/bin/view/Atlas/PanDA',
    packages=['cacheschedconfig'],
    data_files=[
                # crontab file
                ('/etc/cron.d', ['cron/cacheschedconfig',
                                       ]
                 ),
                # Utility wrapper script and main script
                ('/opt/cacheschedconfig/bin', ['bin/cacheSC.sh',
                                               'bin/cacheSchedConfig.py',
                                               ]
                 ),
                ('/opt/cacheschedconfig/etc/sysconfig', ['etc/cacheschedconfig-sysconfig',
                                                         ]
                 ),
                ]
)
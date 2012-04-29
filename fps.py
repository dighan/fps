#!/usr/bin/env python

import sys
import os
import re
import ConfigParser
from optparse import OptionParser

class FPSError(Exception):
    pass

class FPSPath(object):
    BASE = os.getcwd() + os.sep
    CONFIG = BASE + 'config.cfg'
    ARCHIVES = BASE  + 'archives' + os.sep

class FPSInstaller(object):
    def __init__(self, config):
        self.config = config
        self.versions = self.get_versions()

    def get_versions(self):
        return sorted([version for version in os.listdir(FPSPath.ARCHIVES)], reverse = True)

    def parse_version(self, raw_version):
        if not re.match('^\d{2}(\.\d(\.\d{3}(\.\d{1,3})?)?)?$', raw_version):
            raise FPSError('Invalid version pattern.')

        complete_version = None

        for version in self.versions:
            if version.startswith(raw_version):
                complete_version = version
                break

        return complete_version

    def install(self, version):
        complete_version = self.parse_version(version)

        if not complete_version:
            raise FPSError('Version %s does not exists' % (version))

        if sys.platform != 'darwin':
            raise FPSError('Current platform is not yet supported (only Mac OS X).')

        install_dir = self.config.get(sys.platform, 'install_dir')

        # create install_dir if not exists
        # unzip/untar archive file
        # copy archive content to install_dir (manage permissions)

        print 'Flash Player ' + complete_version + ' has been successfully installed !'

def main(options, args):
    if len(args) != 1:
        raise FPSError('Missing argument : version is required.')

    config = ConfigParser.SafeConfigParser()
    config.read(FPSPath.CONFIG)

    installer = FPSInstaller(config)
    installer.install(args[0])

if __name__ == '__main__':
    try:
        parser = OptionParser()
        main(*parser.parse_args())
    except FPSError, exception:
        print exception

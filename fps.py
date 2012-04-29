#!/usr/bin/env python

import sys
import os
import re
import ConfigParser
from optparse import OptionParser

BASE_DIR = os.getcwd() + os.sep
CONFIG_DIR = BASE_DIR + 'config.cfg'
VERSIONS_DIR = BASE_DIR  + 'versions' + os.sep 

class FPSInstaller(object):
    def __init__(self, config):
        self.config = config
        self.versions = self.get_versions()

    def get_versions(self):
        versions = []

        for version in os.listdir(VERSIONS_DIR):
            versions.append(version)

        versions.sort(reverse = True)

        return versions

    def parse_version(self, raw_version):
        matches = re.match('^\d{2}(\.\d(\.\d{3}(\.\d{1,3})?)?)?$', raw_version)

        if matches == None:
            raise RuntimeError('Invalid pattern.')

        complete_version = None

        for version in self.versions:
            if version.startswith(raw_version):
                complete_version = version
                break

        return complete_version

    def install(self, version):
        complete_version = self.parse_version(version)

        if complete_version == None:
            raise RuntimeError('No version available.')

        if sys.platform != 'darwin':
            raise RuntimeError('Platform not yet supported (only Mac OS X).')

        install_dir = self.config.get(sys.platform, 'install_dir')

        if not os.path.exists(install_dir):
            os.mkdir(install)

        command = 'sudo cp -r "%s" "%s"' % (VERSIONS_DIR + complete_version + os.sep, install_dir)
        os.system(command)

        print 'Flash Player ' + complete_version + ' has been successfully installed !'

def main(options, args):
    if len(args) != 1:
        raise RuntimeError('Missing argument : version argument expected.')

    config = ConfigParser.SafeConfigParser()
    config.read(CONFIG_DIR)

    installer = FPSInstaller(config)
    installer.install(args[0])

if __name__ == '__main__':
    try:
        parser = OptionParser()
        main(*parser.parse_args())
    except RuntimeError, exception:
        print exception

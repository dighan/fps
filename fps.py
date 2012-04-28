#!/usr/bin/env python

import sys
import os
import re
import shutil
import ConfigParser
from optparse import OptionParser

BASE_DIR = os.getcwd() + os.sep
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
            raise RuntimeError('Invalid pattern')

        parsed_version = None

        for version in self.versions:
            if version.startswith(raw_version):
                parsed_version = version
                break

        return parsed_version

    def install(self, version):
        parsed_version = self.parse_version(version)

        if parsed_version == None:
            raise RuntimeError('No version available')

        if not self.config.has_section(sys.platform):
            raise RuntimeError('Platform not yet supported')

        install_dir_option = 'install_dir'

        if sys.platform == 'win32' and sys.maxsize > 2**32:
            install_dir = 'install_64bits_dir'

        install_dir = self.config.get(sys.platform, install_dir_option)

        if not os.path.exists(install_dir):
            os.mkdir(install)

        # do the same for win32
        os.system('sudo cp -r ' + VERSIONS_DIR + parsed_version + os.sep + ' ' + install_dir)

        print 'Flash Player ' + parsed_version + ' has been successfully installed !'

def main(options, args):
    if len(args) != 1:
        raise RuntimeError('Missing argument : version argument expected')


    # loads installers.cfg file
    config = ConfigParser.SafeConfigParser()
    config.read(BASE_DIR + 'installers.cfg')

    # installs requested Flash Player version
    installer = FPSInstaller(config)
    installer.install(args[0])

if __name__ == '__main__':
    try:
        parser = OptionParser()
        main(*parser.parse_args())
    except RuntimeError, e:
        print e

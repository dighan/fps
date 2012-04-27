#!/usr/bin/env python

from optparse import OptionParser

class FPSLocation(object):
    ARCHIVES = './archives/'
    PLUGIN_MACOSX = '/Library/Internet Plug-Ins/'

"""
@todo: manage small & large versions
       support macosx, win32/64 and linux32/64 bits
       auto-create default directories if not exist
       add usage text
"""
class FPSInstaller(object):
    def __init__(self, os):
        self.os = os

    def install(self, version):
        if not self.has_version(version):
            raise RuntimeError('No version available')

        print self.os + ' ' + version

    def has_version(self, version):
        return True

def main(options, args):
    if len(args) != 1:
        raise RuntimeError('Argument expected : flash player version')

    installer = FPSInstaller('macosx')
    installer.install(args[0])

if __name__ == '__main__':
    try:
        parser = OptionParser()
        main(*parser.parse_args())
    except RuntimeError, e:
        print e

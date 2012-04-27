#!/usr/bin/env python

import optparse

class FPSLocation(object):
    ARCHIVES = './archives/'
    PLUGIN_MACOSX = '/Library/Internet Plug-Ins/'

class FPSInstaller(object):
    def __init__(self, os):
        self.os = os

    def install(self, version):
        print version

def main(parser):
    (opts, args) = parser.parse_args()

if __name__ == '__main__':
    main(optparse.OptionParser())

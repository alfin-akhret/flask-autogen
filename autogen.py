#!/usr/bin/env python
# CLI client for markweb app
# @author: alfin akhret
# features:
# 1. fetch the markweb skeleton

"""Naval Fate.

Usage:
  markweb install [--target=PROJECT_FOLDER]
  markweb --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt
from autogen_libs.scafolder import Scafolder
import sys 

def install(target=None):
    if target:
        scafolder = Scafolder(target)
        # scafolder.install()
    else:
        print 'No target folder specified'
        sys.exit(1)

if __name__ == '__main__':
    args = docopt(__doc__, version='Markweb 0.0.1')
    # print args
    if args['install']:
        install(args['--target'])

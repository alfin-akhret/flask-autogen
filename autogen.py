#!/usr/bin/env python
# CLI client for markweb app
# @author: alfin akhret
# features:
# 1. fetch the markweb skeleton

"""Naval Fate.

Usage:
  autogen install [--target=PROJECT_FOLDER, --type=PROJECT_TYPE]
  autogen --version

Options:
  -h --help     Show this screen.
  --version     Show version.

"""
from docopt import docopt
from autogen_libs.scafolder import Scafolder
import sys 

def install(target=None, project_type=None):
    if target:
        scafolder = Scafolder(target, project_type)
        scafolder.install()
    else:
        sys.exit(1)

if __name__ == '__main__':
    args = docopt(__doc__, version='Autogen 0.0.1')
    # print args
    if args['install']:
        install(args['--target'], args['--type'])

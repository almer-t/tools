#!/usr/bin/env python3
#
# regex-refspam-gen.py: Automagically create a regular expression that can be used to filter out referrer spam.
#
# Usage:
#   ./regex-refspam-gen.py --input-source-url URL
#
# A sane default input url is used.
# The output is printed to the console and can be used directly
# in e.g. an analytics console.
#
# This script was inspired by:
# * https://gist.github.com/reederz/b0aa902dc2dbe87b5a4c
# * http://stephsharp.me/blocking-referrer-spam/
# * https://github.com/piwik/referrer-spam-blacklist 
#
# Copyright (C) Almer S. Tigelaar <firstname at lastname dot net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import argparse
import urllib.request
import os.path
import re

parser = argparse.ArgumentParser(description='Generate a referrer spam regex')

parser.add_argument('--input-source-url', '-i', dest='input_url', metavar='URL', help='Input source file (assumed to have one hostname per line)')

parser.set_defaults(input_url='https://raw.githubusercontent.com/piwik/referrer-spam-blacklist/master/spammers.txt')
args = parser.parse_args()

if args.input_url is None:
    print('You must provide an input URL')
    exit(1)

c = 0
parts = []
with urllib.request.urlopen(args.input_url) as fi:
    for l in fi:
        h = l.decode('utf8').strip()
        parts.append(re.escape(h))
        c += 1
print('Completed. {0} entries processed'.format(c))
print('Regex:\n{0}'.format('|'.join(parts)))

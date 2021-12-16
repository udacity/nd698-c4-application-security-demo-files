#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# hashid.py - Software to identify the different types of hashes
# Copyright (C) 2013-2015 by c0re <c0re@psypanda.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import io
import os
import re
import sys
import argparse
from collections import namedtuple

__author__  = "c0re"
__version__ = "3.2.0-dev"
__github__  = "https://github.com/psypanda/hashID"
__license__ = "License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>"
__banner__  = "hashID v{0} by {1} ({2})".format(__version__, __author__, __github__)

Prototype = namedtuple('Prototype', ['regex', 'modes'])
HashInfo = namedtuple('HashInfo', ['name', 'hashcat', 'john', 'extended'])

prototypes = [
    Prototype(
        regex=re.compile(r'^[a-f0-9]{32}(:.+)?$', re.IGNORECASE),
        modes=[
            HashInfo(name='MD5', hashcat=0, john='raw-md5', extended=False)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{40}(:.+)?$', re.IGNORECASE),
        modes=[
            HashInfo(name='SHA-1', hashcat=100, john='raw-sha1', extended=False)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{64}(:.+)?$', re.IGNORECASE),
        modes=[
            HashInfo(name='SHA-256', hashcat=1400, john='raw-sha256', extended=False)]),
    Prototype(
        regex=re.compile(r'^[a-f0-9]{128}(:.+)?$', re.IGNORECASE),
        modes=[
            HashInfo(name='SHA-512', hashcat=1700, john='raw-sha512', extended=False)])
]

class HashID(object):

    """HashID with configurable prototypes"""

    def __init__(self, prototypes=prototypes):
        super(HashID, self).__init__()

        # Set self.prototypes to a copy of prototypes to allow
        # modification after instantiation
        self.prototypes = list(prototypes)

    def identifyHash(self, phash):
        """Returns identified HashInfo"""
        phash = phash.strip()
        for prototype in self.prototypes:
            if prototype.regex.match(phash):
                for mode in prototype.modes:
                    yield mode

    def writeResult(self, identified_modes):
        """Write human readable output from identifyHash"""
        count = 0
        hashTypes = []
        for mode in identified_modes:
            count += 1
            hashTypes.append({'name':mode.name, 'hashcat': mode.hashcat, 'jtr': mode.john})

        if count == 0:
            return []
        return hashTypes
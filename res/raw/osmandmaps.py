#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  osmandmaps.py
#
#  Copyright 2013 strannik <mail@strannik-j.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#


from zipfile import ZipFile
from sys import exit
from re import compile as _compile, IGNORECASE, VERBOSE
from os import utime, remove
from time import mktime
from config import *
from operator import truth
from urllib import urlopen


def get_urls(url_str):
    x = urlopen(url_str)
    list_str = x.read()
    y = _compile(
        '''<a\s+href=(?P<quote>["'])?(?P<obf>[^"']+)(?(quote)(?P=quote))[^>]*?>''', IGNORECASE | VERBOSE)
    urls_M = []
    for i in y.finditer(list_str):
        urls_M.append(i.group('obf'))
    return urls_M


def get_names(urls_M):
    maps_D = {}
    maps_M = []
    for i in urls_M:
        if 'zip' in i:
            maps_D[i[32:]] = i[32:i.find('_')] + ' - ' + i[i.find('_') + 1:-10]
            maps_M.append(i[32:])
    return maps_M, maps_D


def create_url(i):
    x = 'http://download.osmand.net/download.php?standard=yes&file={0}'.format(
        i)
    return x


def download_files(xmaps_M, download_path=pwd):
    print 'download_files'
    for i in xmaps_M:
        y = create_url(i)

        print 'i = ', i
        print 'y = ', y
        try:
            web_file = urlopen(y)
            print 'webfile open'
            local_file = open(path.join(download_path, i), 'wb')
            r = None
            while r != '':
                r = web_file.read(1024)
                local_file.write(r)
            web_file.close()
            local_file.close()
        except:
            print 'except'
            exit()


def unzip(xmaps_M, download_path=pwd, extract_path=pwd):
    for i in xmaps_M:
        fh = open(path.join(download_path, i), 'rb')
        z = ZipFile(fh)
        for f in z.infolist():

            name, date_time = f.filename, f.date_time
            print name
            if name[-3:] == 'obf':
                name = path.join(download_path, name)
                with open(name, 'wb') as outFile:
                    outFile.write(z.open(f).read())
                date_time = mktime(date_time + (0, 0, -1))
                utime(name, (date_time, date_time))
        remove(path.join(download_path, i))


def main(url_str):
    urls_M = get_urls(url_str)
    maps_M, maps_D = get_names(urls_M)
    files_M = create_url(maps_M)
    # download_files(files_M)
    # unzip(files_M)


if __name__ == '__main__':
    main(url_str)
else:
    print 'import download module'

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  config.py
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
#  config for osmandmaps

from os import path, getcwd

url_str = "http://download.osmand.net/list.php"
download_path = '/sdcard/osmand'
extract_path = '/sdcard/osmand'

pwd = getcwd()


def __init__():
    print 'INIT'
    global download_path
    global extract_path
    if not path.exists(download_path):
        download_path = pwd

    if not path.exists(extract_path):
        extract_path = pwd
    print 'download path: ', download_path
    print 'extract path: ', extract_path


def main():

    return 0

if __name__ == '__main__':
    main()

if __name__ == 'config':
    print 'import config'
    __init__()

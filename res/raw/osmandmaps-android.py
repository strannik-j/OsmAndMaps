#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  osmandmaps-android.py
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
#  andoir gui for osmandmaps

from android import Android
from osmandmaps import *


def gui(maps_M):
    xmaps_M = []
    droid = Android()
    droid.dialogCreateAlert('Checkbox')
    droid.dialogSetMultiChoiceItems(maps_M)
    droid.dialogSetPositiveButtonText('Download')
    droid.dialogShow()

    while not droid.dialogGetResponse().result['which'] == 'positive':
        pass
    xmaps_num = droid.dialogGetSelectedItems().result
    print(xmaps_num)
    for i in xmaps_num:
        xmaps_M.append(maps_M[i])
    return xmaps_M


def main():
    urls_M = get_urls(url_str)
    maps_M, maps_D = get_names(urls_M)
    xmaps_M = gui(maps_M)
    download_files(xmaps_M, download_path)
    print 'download coplite'
    unzip(xmaps_M, download_path, extract_path)

    print 'unzip complit'

    return 0

if __name__ == '__main__':
    print 'OsmAnd Maps Downloader'
    main()

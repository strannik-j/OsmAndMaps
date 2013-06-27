#!/bin/bash

package=$1
package_dir=$(echo src/$package|sed 's/\./\//g')
mkdir -p $package_dir
mv src/com/strannikj/osmandmaps/* $package_dir/
rmdir src/com/strannikj/osmandmaps
rmdir src/com/strannikj
rmdir src/com
source_files=$package_dir/*
for filename in $source_files AndroidManifest.xml build.properties;
do
	sed 's/com\.strannikj\.osmandmaps/'$package'/g' $filename > tmp; mv tmp $filename;
done

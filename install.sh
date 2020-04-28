#!/bin/bash
filename=`pwd`'/deadlines'
chmod 777 $filename
ln -s $filename /usr/local/bin/deadlines
echo "Done!"
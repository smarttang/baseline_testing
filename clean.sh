#!/bin/bash
#######################
#
#  clean local script
#
#######################

/bin/rm -rf {lib,plugins}/*.pyc
/bin/rm -rf report/html/*.html
/bin/rm -rf report/xml/*.xml
/bin/rm -rf report/tar/*.tar.gz
/usr/bin/touch report/html/test.html
/usr/bin/touch report/xml/test.xml
/usr/bin/touch report/tar/test.tar.gz
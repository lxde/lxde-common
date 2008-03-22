#!/usr/bin/env python
import os, sys
os.system( 'fdupes -r nuoveXT2 > dups.txt' )

excludes=['gnome', 'redhat', 'xfce', 'mozilla', 'thunderbird', 'evolution', 'rythmbox', 'stock', 'gtk']

def is_not_generic( file ):
    for exclude in excludes:
        if file.find( exclude ) != -1:
            return True

    if os.path.basename(file).startswith('k'): # don't use kde icon
        return True

    return False

def get_common_dir( path1, path2 ):

    while path1 != '' and path2 != '':
        path1 = os.path.dirname(path1)
        path2 = os.path.dirname(path2)
        if path1 == path2:
            return path1+'/'

    return ''

def get_relative_path( file, relative_to ):
    prefix = get_common_dir( file, relative_to )
    prefix_len = len(prefix)
    rest = relative_to[ prefix_len : ]
    n = rest.count( '/' )
    prefix=''
    while n > 0:
        prefix += '../'
        n = n - 1
    return prefix + relative_to[ prefix_len : ]


files=[]
f = open( 'dups.txt', 'r' )
generic=''
for line in f:
    file = line.rstrip()
    if file != '':
        if generic != '' or is_not_generic( file ):
            files.append( file )
        else:
            generic = file
    else:
        if generic == '':
            generic = files[0]
            del files[0]
        for file in files:
            print'rm -f %s' % file
            print 'ln -s %s %s' % (get_relative_path(file, generic), file)
        print
        files=[]
        generic=''

f.close()

#!/usr/bin/python
# -*- coding: utf-8 -*-

import re, sys
from telnetconnector import connector
from getopt import getopt

def usage():
    print('\t\t\t-h, --help:  View this message')
    print('\n\t\t\t-EXAMPLE: findnumbervrt.py -n 631234567')
    sys.exit(1)

number = None   
opts, args = getopt(sys.argv[1:], 'hn:',["help","number="])
for o,v in opts:
    if o in ("-h", "--help"):
        usage()
    elif o in ("-n", "--number"):
        number = v
if number is None: number = str(input("Enter phone number: "))
if re.match(r'[6-7,9]{1}[0-9]{8}', number) and len(number) == 9:
    output = connector('list usage digit-string ' + number)
    if len(output) < 128:
        print((output[82:123]).replace('\t', ' '))
    else:
        print('No data in the system to list')
else:
    print('Error in entered number')

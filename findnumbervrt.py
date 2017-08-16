import telnetlib
import re
import sys
from getopt import getopt
from time import sleep

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
    tn = telnetlib.Telnet('10.89.61.20', '5023')
    tn.read_until('login'.encode())
    tn.write('dadmin\n'.encode())
    tn.read_until('Password'.encode())
    tn.write('dadmin01\n'.encode())
    tn.read_until('Pin'.encode())
    tn.write('dadmin01\n'.encode())
    tn.read_until('Terminal'.encode())
    tn.write('ossi\n'.encode())
    tn.read_until('t\n'.encode())
    tn.write(('clist usage digit-string ' + number + '\n').encode())
    tn.write('t\n'.encode())
    output = tn.read_until('t\n'.encode())
    if len(output) < 128:
        print((output[82:123]).decode('utf-8').replace('\t', ' '))
    else:
        print('No data in the system to list')
    tn.write('clogoff\n'.encode())
    tn.write('t\n'.encode())
    sleep(0.1)
    tn.write('y\n'.encode())
else:
    print('Error in entered number')

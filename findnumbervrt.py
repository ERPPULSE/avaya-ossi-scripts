import telnetlib
import sys
from getopt import getopt
from time import sleep

def usage():
    print '\t\t\t-h, --help:  View this message'
    print '\n\t\t\t-EXAMPLE: findnumbervrt.py -n 631234567'
    sys.exit(1)
    
number = None    
opts, args = getopt(sys.argv[1:], 'hn:',["help","number="])
for o,v in opts:
    if o in ("-h", "--help"):
        usage()
    elif o in ("-n", "--number"):
        number = v
if number is None: number = raw_input("Enter phone number: ") 
'''Conector'''
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
tn.write('clist usage digit-string ' + number + '\n'.encode())
tn.write('t\n'.encode())
output = tn.read_until('t\n'.encode()).encode('utf-8')
try:
    print 'Number ' + number + ' found in VRT: %s, position: %s' %(output[103:].split('\t')[1],output[103:].split('\t')[3][:2])
except IndexError:
    print 'Number ' + number + ' not found'
'''Logout'''
tn.write('clogoff\n')
tn.write('t\n')
sleep(0.1)
tn.write('y\n')

import telnetlib
import re
from time import sleep

def paramset(co, fi, par):
    if co[:2] == 'ch':
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
        tn.write(('c' + str(co) + '\n').encode())
        tn.write((str(fi) + '\n').encode())
        tn.write(('d' + str(par) + '\n').encode())
        tn.write('t\n'.encode())
        tn.write('clogoff\n'.encode())
        tn.write('t\n'.encode())
        sleep(0.2)
        tn.write('y\n'.encode())
    else:
        print('Error in first function parameter')

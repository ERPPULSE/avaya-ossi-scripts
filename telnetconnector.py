#!/usr/bin/python
# -*- coding: utf-8 -*-

import telnetlib
from time import sleep

def connector(co):
    comm = 'c' + str(co) + '\n'
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
    tn.write(comm.encode())
    tn.write('t\n'.encode())
    output = tn.read_until('t\n'.encode()).decode('utf-8')
    tn.write('clogoff\n'.encode())
    tn.write('t\n'.encode())
    sleep(0.2)
    tn.write('y\n'.encode())
    return output

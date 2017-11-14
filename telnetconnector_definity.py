#!/usr/bin/python
# -*- coding: utf-8 -*-
# python v.2

import telnetlib
from time import sleep

def connector(co):
    comm = 'c' + str(co) + '\n'
    tn = telnetlib.Telnet('172.16.0.162', '5022',10)
    tn.read_until('Login:')
    tn.write('yoursuperloginname'.encode('ascii') + "\r\n".encode('ascii'))
	sleep(0.2)
    tn.read_until('Password:')
    tn.write('yoursuperpassword'.encode('ascii') + "\r\n".encode('ascii'))
    tn.read_until('Terminal')
    tn.write('ossi'.encode('ascii') + "\r\n".encode('ascii'))
    tn.read_until('t\n')
    tn.write(comm.encode('ascii') + "\r\n".encode('ascii'))
    tn.write('t'.encode('ascii') + "\r\n".encode('ascii'))
    output = tn.read_until('t\n').encode('utf-8')
    tn.write('clogoff\n')
    tn.write('t\n')
    sleep(0.2)
    tn.write('y\n')
    return output
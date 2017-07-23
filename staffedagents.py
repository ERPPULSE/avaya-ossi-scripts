#!/usr/bin/python

import telnetlib
from time import sleep

'''Login into station and activate OSSI'''
tn = telnetlib.Telnet('10.89.61.20', '5023')
tn.read_until('login')
tn.write('dadmin\n')
tn.read_until('Password')
tn.write('dadmin01\n')
tn.read_until('Pin')
tn.write('dadmin01\n')
tn.read_until('Terminal')
tn.write('ossi\n')
tn.read_until('t\n')
tn.write('clist agent-loginID\n')
tn.write('t\n')
output = tn.read_until('t\n').encode('utf-8')
'''Find in output data agent's stations and count how many whey are'''
res = 0
for i in range(5801,5822,1):
        res += output.count(str(i))

'''Logoff OSSI'''
tn.write('clogoff\n')
tn.write('t\n')
sleep(0.1)
tn.write('y\n')

print "Staffed agents: %s" % (res)

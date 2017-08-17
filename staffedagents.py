import telnetlib
from telnetconnector import connector

output = connector('li age')
'''Find in output data agent's stations and count how many they are'''
res = 0
for i in range(5801,5822,1):
        res += output.count(str(i))
print ("Staffed agents: %s" % (res))

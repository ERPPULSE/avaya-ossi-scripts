import re
from telnetconnector import connector

output = connector('monitor bcms skill 1')
print ("Calls waiting: %s" % (re.search('s\t(.*)\t', output).group(1)))

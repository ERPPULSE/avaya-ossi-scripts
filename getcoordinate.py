import telnetlib

comm = 'c' + str(input('Enter command to get field address:')) + '\n'
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

fields = {}
data = {}
lines = output.split('\n')
for line in lines:
    if line.startswith('d'):
        data.update({
            len(data): line[1:]
	})
    elif line.startswith('f'):
        fields.update({
	    len(fields): line[1:]
	})
    elif line.startswith('t'):
        break
    else:
        pass
parse = {
    'fields': fields,
    'data': data,
}
result = {} 
for i in range(len(parse['fields'])):
    fids = parse['fields'][i].split('\t')
    data = parse['data'][i].split('\t')
    for i in range(len(fids)):
        result.update({
            fids[i]: data[i]
        })
print (result)

from telnetconnector import connector

output = connector(str(input('Enter command to get field address:')))
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

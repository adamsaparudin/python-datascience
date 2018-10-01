person = dict()
while True:
	key = input('input key: ')
	if key == 'stop': break
	val = input('input value: ')
	if person.get(key) != None:
		if(type(person.get(key)) == str):
			person[key] = [person[key], val]
		else:
			person[key].append(val)
	else:
		person[key] = val
print(person)

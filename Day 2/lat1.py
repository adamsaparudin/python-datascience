person = dict()
while True:
	key = input('input key: ')
	if key == 'stop': break
	val = input('input value: ')
	if key == 'makanan':
		if person.get(key) == None:
			person[key] = [val]
		else:
			person[key].append(val)
	else:
		person[key] = val
print(person)

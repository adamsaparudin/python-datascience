person = dict()
while True:
	key = input('Enter key: ')
	val = input('Enter val: ')
	if key == 'stop': break
	person[key] = val
	print(person)

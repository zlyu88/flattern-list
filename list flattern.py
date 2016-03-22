lst = [1, 8, [2, 3], 4, [[6, 7]]]

def simple_list(lst):
	new_list = []
	for number in lst:
		if type(number) == int:
			new_list.append(number)
		elif type(number) == list:
			new_list.extend(simple_list(number))
	return new_list
	
print simple_list(lst)




# SAN DARATING
def find_unique(id_array):
	uniques = []
	id_array.sort()
	for index, item in enumerate(id_array):
		left_flag = False
		right_flag = False
		if index - 1 < 0:
			left_flag = True
		else:
			if id_array[index - 1] == item:
				left_flag = True
		if index + 1 >= len(id_array):
			right_flag = True
		else:
			if id_array[index + 1] == item:
				right_flag = True
		if not(left_flag or right_flag):
			uniques.append(item)
	return uniques






delivery_id_confirmations = [8,1,2,3,4,5,6,7,9,3,2,1,4,6,7,9,8]

print(find_unique(delivery_id_confirmations))
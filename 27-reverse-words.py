def reverse_words(message_char_list):
	words_unreversed = []
	current_string = ''
	for index, character in enumerate(message_char_list):
		if character == ' ':
			words_unreversed.append(current_string)
			current_string = ''
		elif index == len(message_char_list) - 1:
			current_string += character
			words_unreversed.append(current_string)
			current_string = ''
		else:
			current_string += character
	message_char_list.clear()
	for word in words_unreversed:
		message_char_list.insert(0, word)



message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print(message)
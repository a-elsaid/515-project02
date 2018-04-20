from dic import dictionary
def word_count(str):
	dic 	= dictionary()
	counts 	= dict()
	words 	= str.split()
	for word in words:
		print word
		if word in dic:
			if word in counts:
				counts[word] += 1
			else:
				counts[word] = 1
	return counts


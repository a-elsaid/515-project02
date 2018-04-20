import numpy as np

file = open('stopwords_raw.txt', 'rb')

file = file.read().replace('\n', ' ')
file = file.split(' ')
f = []
for i in file:
	if i!='':
		f.append(i)

np.save('stop_words', f)

from load_webpage import load_pg
from dic import dictionary
import numpy as np

url         = 'http://wenchen.cs.und.edu/course/515/9/5.html'

stop_words  = np.load('stop_words.npy')

page        = load_pg(url)
print page
for s_w in stop_words:
    if len(s_w)!=1:
        pass
    # page = page.replace(' ' + s_w, '-')
    page = page.replace(' ' + s_w + ' ', ' ')
    # page = page.replace(s_w + ' ', '-')

print page
DIC         = dictionary()

from count_words import word_count

print word_count(page)
 






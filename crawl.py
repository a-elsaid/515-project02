from os import popen
from sys import argv
SEED_URL    = argv[1]
MAX_URLS    = 500
MAX_DEPTH   = 3

SEED_URL = SEED_URL.split('//')
if len(SEED_URL)>1:
    SEED_URL = SEED_URL[1]
else:
    SEED_URL = SEED_URL[0]

def fetch_link_list(url):
    cmd = "lynx -dump -listonly " + url  +  " |  awk '/http/{print $2}'"
    sub_urls = popen(cmd).read().split("\n")
    sub_urls = set(sub_urls)
    return list(set([x for x in sub_urls if len(x)!=0 and '#' not in x and SEED_URL in x]))



sub_urls = fetch_link_list(SEED_URL)


print "Total Number of Pages form Lynx: ", len(sub_urls)

Final_URLs = sub_urls
flg = 0
counter = len(Final_URLs)
for level in range(MAX_DEPTH):
    level_urls = []
    if flg==1:
        break
    for link in sub_urls:
        if flg ==1:
            break
        print link
        # print "LINK: ", link
        links_list = fetch_link_list(link)
        level_urls.append(links_list)
        for l in list(set(links_list)):
            if l not in Final_URLs:
                Final_URLs.append(l)
                counter+=1
                print counter
                print "size of Final_URLs: ", len(Final_URLs)
                if counter==MAX_URLS:

                    flg=1
                    break
    sub_urls = list(set([y for x in level_urls for y in x]))
    print "Lenth of level-{}_urls: ".format(level), len(sub_urls)

for i in Final_URLs:
    if Final_URLs.count(i)>1:
        print "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
        print "GGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG"
















exit()

from BeautifulSoup import BeautifulSoup
import urllib



SEED_URL = 'http://' + SEED_URL
print "DDDDDDD: ", SEED_URL
url_content = urllib.urlopen(SEED_URL)
soup = BeautifulSoup(url_content)
title = soup.title.string
print title




exit()
sub_urls = soup.findAll('a')

sub_urls = [str(x.get('href')) for x in sub_urls]
sub_urls = [x for x in sub_urls if len(x)!=0 and "#" not in x]
# and x.split('.')[-1] not in ['wav', 'jpg', 'jpeg', 'png', 'mp3', 'pdf', 'txt']

sub_urls2=set(sub_urls)
# and SEED_URL in x


print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
print "Total Number of pages from BeautufulSpoup: ",  len(sub_urls2)

print (len(sub_urls1)- len(sub_urls2))

for i in sub_urls2:
    if i not in sub_urls1:
        print i

exit()


for link in sub_urls:
    url = link
    cmd = "lynx -dump -listonly " + url  +  " |  awk '/http/{print $2}'"
    try:
        sub_urls = popen(cmd).read().split("\n")
    except:
        print "ERROR"

# for depth in range(MAX_DEPTH):



exit()










def dump_links(url):
    cmd = "lynx -dump " + url  +  " |  awk '/http/{print $2}'"
    sub_urls = popen(cmd).read().split('\n')
    return sub_urls

def breadth_crawl(links, count, depth):
    counter = count
    links_collection = []
    for l in links:
        if counter>=MAX_URLS:
            break
        print l
        print "DEPTH: {}   -   COUNTER: {}".format(depth, counter)
        links_collection.append(dump_links(l))
        counter+=1
    return counter

def depth_crawl(collection,depth, count):
    counter = count
    if counter<MAX_URLS:
        for lnks in collection:
            if depth<MAX_DEPTH:
                counter = breadth_crawl(lnks, counter, depth+1)
                depth+=1





depth_crawl(dump_links(URL), 1, 2)

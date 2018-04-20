import os



def load_pg(url):
    return os.popen('lynx -dump ' + url).read()



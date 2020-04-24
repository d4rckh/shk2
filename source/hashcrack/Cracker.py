import threading
from Logger import *

class Cracker:
    
    def __init__(self, hash, wordlist, cfunc, finish):
        self.hash = hash
        self.wordlist = wordlist
        self.x = None
        self.cfunc = cfunc
        self.finish = finish
        self.finished = False

    def th(self, h, wl, cfunc, finish):
        for w in wl:
            #print("Checking " + w)
            crack("PH", str(h), str(w))
            if cfunc(w) == h:
                finish(h, w, True)
                self.finished = True
                return
        self.finished = True
        finish(h, None, False)


    def start(self):
        x = threading.Thread(target=self.th, args=(self.hash,self.wordlist,self.cfunc,self.finish,)) 
        x.start()
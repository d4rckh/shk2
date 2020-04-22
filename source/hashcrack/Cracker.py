import threading

class Cracker:
    
    def __init__(self, hash, wordlist, cfunc, finish):
        self.hash = hash
        self.wordlist = wordlist
        self.x = None
        self.cfunc = cfunc
        self.finish = finish

    def th(self, h, wl, cfunc, finish):
        for w in wl:
            if cfunc(w) == h:
                finish(h, w)

    def start(self):
        x = threading.Thread(target=self.th, args=(self.hash,self.wordlist,self.cfunc,self.finish,)) 
        x.start()
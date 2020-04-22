import sys
sys.path.append("./source")
from parseArguments import Parse as parseArguments
from hashcrack.parseHashes import parseHashes
from hashcrack.Cracker import Cracker
from hashcrack.encryptors.encindex import getFunc
from Logger import *

args = parseArguments()

class CrackerMain:
    def __init__(self, wordlist, hashes):
        self.hashes = hashes
        self.wordlist = wordlist
        self.crackers = []
        self.done = 0
        self.failed = 0
        self.success = 0
        self.results = []

    def finish(self, h, w, success):
        stopThread(self.hashes.index(h))
        if success == True:
            self.success += 1
            self.results.append(h + ":" + w)
            foundMatch(self.hashes.index(h), h, w)
            #print("found solution for " + h + " = " + str(w))
        else:
            self.failed += 1
            noMatch(self.hashes.index(h), h)
            #print("fail :(")
        self.done += 1
        if self.done == len(self.hashes):
            finishSession(None)

    def spawnCracker(self,hash):
        CrackingThread = Cracker(hash, ["cookie"], getFunc(args.type), self.finish)
        CrackingThread.start()
        self.crackers.append(CrackingThread)

    def spawnCrackers(self):
        for hash in self.hashes:
            startThread(self.hashes.index(hash), hash)
            self.spawnCracker(hash)

def start():
    with open(args.hashes, "r") as hashesFile:
        hashes = parseHashes(hashesFile.read())
        Session = CrackerMain(["cookie"], hashes)
        Session.spawnCrackers()

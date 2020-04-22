import sys
sys.path.append("./source")
from parseArguments import Parse as parseArguments
from hashcrack.parseHashes import parseHashes
from hashcrack.Cracker import Cracker
from hashcrack.encryptors.encindex import getFunc
from Logger import *
from datetime import datetime

args = parseArguments()

class CrackerMain:
    def __init__(self, wordlist, hashes, file):
        self.hashes = hashes
        self.wordlist = wordlist
        self.crackers = []
        self.file = file
        self.done = 0
        self.failed = 0
        self.success = 0
        self.results = []
        self.st = None
        self.fs = None
        self.delta = None

    def finish(self, h, w, success):
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
        stopThread(self.hashes.index(h))
        if self.done == len(self.hashes):
            self.fs = datetime.now()
            self.delta = self.st - self.fs
            finishSession(None)
            showStats(self)

    def spawnCracker(self,hash):
        CrackingThread = Cracker(hash, ["cookie"], getFunc(args.type), self.finish)
        CrackingThread.start()
        self.crackers.append(CrackingThread)

    def spawnCrackers(self):
        self.st = datetime.now()
        for hash in self.hashes:
            startThread(self.hashes.index(hash), hash)
            self.spawnCracker(hash)

def start():
    with open(args.hashes, "r") as hashesFile:
        hashes = parseHashes(hashesFile.read())
        Session = CrackerMain(["cookie"], hashes, args.hashes)
        Session.spawnCrackers()

import sys
sys.path.append("./source")
from parseArguments import Parse as parseArguments
from hashcrack.parseHashes import parseHashes
from hashcrack.Cracker import Cracker
from hashcrack.encryptors.encindex import getFunc

args = parseArguments()

class CrackerMain:
    def __init__(self, wordlist, hashes):
        self.hashes = hashes
        self.wordlist = wordlist
        self.crackers = []

    def spawnCracker(self,hash):
        CrackingThread = Cracker(hash, ["cookie"], getFunc(args.type))
        CrackingThread.start()
        self.crackers.append(CrackingThread)

    def spawnCrackers(self):
        for hash in hashes:
            self.spawnCracker(hash)

def start():
    with open(args.hashes, "r") as hashesFile:
        hashes = parseHashes(hashesFile.read())
        Session = CrackerMain(["cookie"], hashes)
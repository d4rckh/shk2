import sys
sys.path.append("./source")
from parseArguments import Parse as parseArguments
from banner import show as printBanner
from hashcrack.hashcracker import start as hashcrackStart
args = parseArguments()

printBanner()

if args.vvv:
    print("Ultra verbosity activated\n")

def shk2(): # Main
    if args.hashcrack == True:
        hashcrackStart()
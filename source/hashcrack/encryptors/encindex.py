import sys
sys.path.append("source")
import hashcrack.encryptors.md5 as md5

def getFunc(type):
    if type == "md5":
        return md5.enc
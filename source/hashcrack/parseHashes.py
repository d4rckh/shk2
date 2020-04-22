def parseHashes(hashesFile):
    hashes = []
    hashSplit = hashesFile.split('\n')
    for hash in hashSplit:
        hashes.append(hash)
    return hashes
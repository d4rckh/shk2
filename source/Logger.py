class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def startThread(id, hash):
    print("[" + bcolors.OKBLUE + "INFO" + bcolors.ENDC + "] Started thread with ID " + str(id))# + " cracking " + hash)

def stopThread(id):
    print("[" + bcolors.OKBLUE + "INFO" + bcolors.ENDC + "] Thread with ID " + str(id) + " finished.")

def foundMatch(id,h,w):
    print("[" + bcolors.OKGREEN + "HIT " + bcolors.ENDC + "] Thread with ID " + str(id) + " found valid match! " + bcolors.HEADER + h + bcolors.ENDC + ":" + bcolors.OKGREEN + bcolors.BOLD + w + bcolors.ENDC)

def noMatch(id,h):
    print("[" + bcolors.WARNING + "WARN" + bcolors.ENDC + "] Thread with ID " + str(id) + " didn't find a match for hash " + bcolors.FAIL + h + bcolors.ENDC)

def finishSession(ses):
    print("\n[+] FINISHED")

def showStats(ses):
    print("")
    for hash in ses.results:
        print(hash)
    print("")
    print("-"*10 + " FINISHED SESSION " + "-"*10)
    print("Done...............: " + str(ses.done))
    print("Fail...............: " + str(ses.failed))
    print("Success............: " + str(ses.success))
    print("Wordlist entries...: " + str(len(ses.wordlist)))
    print("Hashes.............: " + str(len(ses.hashes)))
    print("Wordlist...........: " + ses.file)
    print("Start date.........: " + str(ses.st))
    print("End date...........: " + str(ses.fs))
    print("Delta date.........: " + str(ses.delta))
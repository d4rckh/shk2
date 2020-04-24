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

def crack(id,h,w):
    print("[" + bcolors.WARNING + "VERB" + bcolors.ENDC + "] Thread" + id + " checked " + h + " with " + w)

def showStats(ses):
    print("")
    for hash in ses.results:
        print(hash)
    print("")
    print("-"*10 + bcolors.HEADER + " FINISHED SESSION " + bcolors.ENDC + "-"*10)
    print("Done        => " + bcolors.OKBLUE + str(ses.done) + bcolors.ENDC)
    print("Fail        => " + bcolors.FAIL + str(ses.failed) + bcolors.ENDC)
    print("Success     => " + bcolors.OKGREEN + str(ses.success) + bcolors.ENDC)
    print("Words       => " + bcolors.OKBLUE + str(len(ses.wordlist)) + bcolors.ENDC)
    print("Hashes      => " + bcolors.HEADER+ str(len(ses.hashes)) + bcolors.ENDC)
    print("Hashes File => " + ses.file)
    print("Start date  => " + bcolors.OKBLUE + str(ses.st) + bcolors.ENDC)
    print("Finish date => " + bcolors.OKBLUE + str(ses.fs) + bcolors.ENDC)
    print("Delta date  => " + bcolors.OKBLUE + str(ses.delta) + bcolors.ENDC)
def startThread(id, hash):
    print("[+] Started thread with ID " + str(id))# + " cracking " + hash)

def stopThread(id):
    print("[-] Thread with ID " + str(id) + " finished.")

def foundMatch(id,h,w):
    print("[!] Thread with ID " + str(id) + " found valid match! " + h + ":" + w)

def noMatch(id,h):
    print("[0] Thread with ID " + str(id) + " didn't find a match for hash " + h)

def finishSession(results):
    print("\n[+] FINISHED")
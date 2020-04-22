import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--hashcrack', action='store_true', help="Use hash cracking mode.")
parser.add_argument('--hashes', help='File containing one hash per new line.')
parser.add_argument('--type', help='Type of the hash.')

def Parse():
    return parser.parse_args()
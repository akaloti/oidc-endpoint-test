from Crypto.PublicKey import RSA

import sys

if len(sys.argv) == 1:
    print("Missing public key file", file=sys.stderr)
    sys.exit(1)

# Helpful source: https://stackoverflow.com/questions/42504079/how-do-you-extract-n-and-e-from-a-rsa-public-key-in-python
f = open(sys.argv[1], "r")
pubkey = RSA.importKey(f.read())
e_bits = bin(pubkey.e)[2:]
n_bits = bin(pubkey.n)[2:]

def print_bytes(bits):
    missing = 8 - len(bits) % 8
    if missing < 8:
        bits = missing * "0" + bits
    byte_slices = []
    while bits != "":
        piece = bits[0:8]
        bits = bits[8:]
        byte_slices.append(piece)
    for bs in byte_slices:
        print(bs, end=' ')
    print()

print("=== e bits ===")
print_bytes(e_bits)
print("=== n bits ===")
print_bytes(n_bits)

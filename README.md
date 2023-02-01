# OIDC Endpoint Test

## Key Generation

Source: https://www.scottbrady91.com/openssl/creating-rsa-keys-using-openssl

``` bash
# Generate private key.
openssl genrsa -out test.key 3072

# Extract public key from private key.
openssl rsa -in test.key -pubout -out test.pub
```

## Determining 'n' and 'e' for JSON Web Key Set

Use the Python script `get_n_and_e_bitstrings.py` to get the bit strings of the 'n' and 'e' of the given RSA public key. Below is an example:

``` bash
$ python3 get_n_and_e_bitstrings.py key1.pub
=== e bits ===
00000001 00000000 00000001
=== n bits ===
11000000 01010001 00010011 01110010 10001100 11011100 01100011 10100100 11000110 11110110 10111100 00110100 01001101 00110011 11000000 01010111 01010000 11001110 01001001 00101010 11101111 01000000 00001001 00101010 10110011 01100001 10111110 11000010 01000000 10011101 01101110 10000100 01110110 00000000 10000101 11011001 01000011 00000110 10100001 10111101 11001001 00001100 01011111 01100010 00000111 00010011 00000010 01010010 10001100 01001000 11101001 01101000 00011001 01100001 11101101 11011001 01011101 11101011 10111001 10111100 10110111 11101100 00001100 10110100 11110110 01001100 00011110 01010100 10011111 10100101 11111011 00001001 01010111 00001000 01011011 11010100 01101000 00010111 11010001 10010001 10100011 11101101 10111111 00000010 01111101 11101100 00001101 11001111 00100000 00111101 10000000 11100011 10111010 11111110 00011100 01010001 10111110 00001100 11110010 01001100 10000001 01010010 11100100 10010001 00001011 01110000 01110001 01100100 00100110 11101100 11110011 00110010 10100111 10011110 10001101 11001111 00001000 11111010 10101000 10101001 11111111 00010011 10100000 01100011 11011111 01001010 10101100 00000111 11001000 11111000 01001010 00011011 11011000 01010111 01010111 01110001 11101001 10011100 00100011 10010110 11111010 00110001 11000111 00001001 01111100 10010011 00111100 01010011 01010101 00111101 00011001 01001101 00010010 00011110 11101001 01001000 11001100 01001100 00100101 11110100 01101011 10011100 10110110 01001100 00000010 00001011 11001001 00110011 11001001 10100100 10010110 10100010 00101100 01000001 00011000 10100111 10001000 00111000 10011010 11101011 10010101 01000000 10000111 10000111 11010011 11010010 01101010 10111110 00101111 10101010 01011100 11011110 00011111 00111111 11011100 10111101 01110100 00101101 01111101 11010111 01101010 00001011 00011001 01101110 11001100 10111100 11111110 00000000 00000011 01011110 10101010 01111111 01001100 00000000 10100000 10101010 10101001 00011100 10000111 11101000 00100100 10100110 00000000 11011110 10001000 10110010 01110010 00011111 10010000 01101111 01011000 01001011 01101000 00111011 10001011 00100101 01110111 10110111 00100110 10100110 00011111 01110011 10110111 01011001 00110010 11100111 01110101 01110110 10111011 01110111 10111001 11001110 11101111 11000101 10100010 00011011 10101110 11110001 00011100 01101111 00000111 00111000 10110100 01110111 11011101 11101010 00011010 11101010 01111011 10100100 00010110 01000000 10011011 01100000 10101111 00111110 01001011 01101011 10000111 01011000 01110011 10111110 11001101 10010010 00101001 00111101 00001110 11101101 01001001 00011100 11000100 10101011 00101100 11001011 10011000 11010101 00110101 00110110 01110110 11001101 01000101 01100011 01111101 11000010 00010111 10101110 10101011 11100000 10010011 11111111 00111011 11000111 00010101 01100100 11100111 11111110 11111101 11110100 01011010 01101111 10001100 11010100 11001000 01001011 11010010 10000011 01110110 00111010 01011010 01000111 10010110 11111110 01000110 10011011 01111010 11111101 11010100 01001100 10000010 01010010 00111011 00111000 10110000 10010100 11110011 10010101 11010110 10001110 01010100 01111000 00100101 00001110 11101011 10000001 01001010 00000000 10011100 10100111 01100001 00001001 00100011 01000001 00001110 11000001 01101100 00001100 11100000 01001101 00011010 10110110 01000110 01011111 11111010 11100101 01101001 10000100 01110111 10100111 00001110 10101011 00011101 00011101 01001101 01010001
```

Plug the 'e' and 'n' bit strings into this website: https://cryptii.com/pipes/base64-to-hex

Use Base64url format.

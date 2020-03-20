import chilkat
import sys

# set ck acess key
glob = chilkat.CkGlobal()
glob.UnlockBundle("Anything for 30-day trial")

crypt = chilkat.CkCrypt2()

crypt.put_CryptAlgorithm("twofish")
# "ecb" / "cbc"
crypt.put_CipherMode("ecb")

# KeyLength [128, 192, 256]
crypt.put_KeyLength(128)

# Twofish has a block size of 16 bytes, so encrypted output is always
# a multiple of 16.
crypt.put_PaddingScheme(0)

# EncodingMode specifies the encoding of the output for
# encryption, and the input for decryption.
# It may be "hex", "url", "base64", or "quoted-printable".
crypt.put_EncodingMode("hex")
# The secret key must equal the size of the key.  For
# 256-bit encryption, the binary secret key is 32 bytes.
# For 128-bit encryption, the binary secret key is 16 bytes.
keyHex = "000102030405060708090A0B0C0D0E0F101112131415161718191A1B1C1D1E1F"
crypt.SetEncodedKey(keyHex,"hex")

# Encrypt a string...
# The input string is 44 ANSI characters (i.e. 44 bytes), so
# the output should be 48 bytes (a multiple of 16).
# Because the output is a hex string, it should
# be 96 characters long (2 chars per byte).
str = input('Encrypt the string: ')
#encStr = crypt.encryptStringENC("The quick brown fox jumps over the lazy dog.")
encStr = crypt.encryptStringENC(str)
print(encStr)

# Now decrypt:
decStr = crypt.decryptStringENC(encStr)
print(decStr)